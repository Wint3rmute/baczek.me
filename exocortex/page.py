import hashlib
import logging
import math
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import markdown
import numpy
import umap
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util

logger = logging.getLogger(__name__)


def sha256_hash_from(string: str) -> str:
    return hashlib.sha256(string.encode()).hexdigest()


class CachingSentenceTransformer:
    def __init__(self):
        self.cache_location = Path("./generated/embeddings_cache")
        self.cache_location.mkdir(parents=True, exist_ok=True)
        self.cache_hits = 0
        self.cache_misses = 0

        self._sentence_transformer: SentenceTransformer | None = None

    def encode(self, content: str):
        hash = sha256_hash_from(content)
        cache_path = (self.cache_location / hash).with_suffix(".npy")
        if cache_path.exists():
            embeddings = numpy.load(cache_path)
            logger.debug("Cache hit for %s", hash)
            self.cache_hits += 1
        else:
            if self._sentence_transformer is None:
                logger.info("Initializing a sentence transformer...")
                # Consider using "all-MiniLM-L6-v2" for slightly lower accuracy and 5x performance
                self._sentence_transformer = SentenceTransformer("all-mpnet-base-v2")

            logger.debug("Cache miss for %s", hash)
            embeddings = self._sentence_transformer.encode([content])[0]
            numpy.save(cache_path, embeddings)
            self.cache_misses += 1

        return embeddings


_sentence_transformer = CachingSentenceTransformer()

RECENTLY_MODIFIED_FILES = subprocess.check_output(
    "git log --pretty=format: --name-only | grep '.md' | awk '!seen[$0]++' | head -n 3",
    shell=True,
).decode()

logger.debug("Recently modified:")
for line in RECENTLY_MODIFIED_FILES.split("\n")[
    :-1
]:  # Last line is empty, skip it with :-1
    logger.debug("-", line)


def was_recently_modified(file_path: Path) -> bool:
    for file in RECENTLY_MODIFIED_FILES.split("\n"):
        if str(file_path) in file:
            return True

    return False


def extract_title(file_path: Path, content: str) -> str:
    title = None

    for line in content.split("\n"):
        if "title: " in line:
            title = line.replace("title: ", "").strip()

    if not title:
        raise ValueError(f"Title not found in {file_path}")

    return title


@dataclass
class RelatedPost:
    similarity: float
    post: "Post"
    # level: int # 1 = very related, 2 less related, etc


@dataclass
class Post:
    title: str
    content: str
    path: Path
    recently_modified: bool

    embeddings: numpy.ndarray
    related_posts: list[RelatedPost] = field(default_factory=list)

    length_normalized: float = 0

    art_relatedness: float = 0
    music_relatedness: float = 0
    computers_relatedness: float = 0

    # To be filled by UMAP
    _x: float | None = None
    _y: float | None = None

    @property
    def x(self):
        if self._x is None:
            raise ValueError("Value of X coordinate not filled")
        return self._x

    @property
    def y(self):
        if self._y is None:
            raise ValueError("Value of Y coordinate not filled")
        return self._y

    @property
    def link(self) -> str:
        post_link = "/" + str(
            self.path.relative_to("content").parent
            / self.path.relative_to("content").stem
        )

        return post_link

    def get_rgb(self) -> tuple[int, int, int]:
        red = 100 + int(155 * self.art_relatedness)
        green = 100 + int(155 * self.computers_relatedness)
        blue = 100 + int(155 * self.music_relatedness)

        return (red, green, blue)

    def get_html_color(self) -> str:
        red, green, blue = self.get_rgb()
        return f"#{red:02x}{green:02x}{blue:02x}"

    @classmethod
    def from_path(cls, path: Path):
        if path.suffix == ".md":
            content_raw = path.read_text()
            # No easy markdown to text convertsion available at the moment :/
            html = markdown.markdown(content_raw)
            html_tree = BeautifulSoup(html, features="html.parser")
            content = html_tree.text

            title = extract_title(path, content_raw)

        elif path.suffix == ".html":
            content_raw = path.read_text()
            html_tree = BeautifulSoup(content_raw, features="html.parser")
            html_tree.nav.decompose()
            content = html_tree.text.replace("\n", "")

            title = path.name

            to_trim = content.rfind("Incoming:")
            if to_trim != -1:
                content = content[to_trim:]

        embeddings = _sentence_transformer.encode(content)
        return cls(
            title=title,
            content=content,
            path=path,
            recently_modified=was_recently_modified(path),
            embeddings=embeddings,
        )

    def __hash__(self) -> None:
        return hash(self.path)

    def distance_to(self, post: "Post") -> float:
        return math.sqrt((self.x - post.x) ** 2 + (self.y - post.y) ** 2)
        # return -util.cos_sim(self.embeddings, post.embeddings)

    def distance_embedding(self, post: "Post") -> float:
        # return math.sqrt((self.x - post.x) ** 2 + (self.y - post.y) ** 2)
        result = -util.cos_sim(self.embeddings, post.embeddings)
        return float(result)


def get_all_posts() -> list[Post]:
    logger.info("Loading pages...")
    all_posts = []
    all_posts_paths = Path.glob(Path("./content/"), "**/*.md")

    for post_path in all_posts_paths:
        all_posts.append(Post.from_path(post_path))

    embeddings = [post.embeddings for post in all_posts]

    umap_result = umap.UMAP().fit_transform(embeddings)
    # umap_result = manifold.TSNE(
    #     n_components=2,
    #     learning_rate='auto',
    #     init='random',
    #     perplexity=3).fit_transform(numpy.array(embeddings))
    # from sklearn.decomposition import PCA
    # umap_result = PCA(n_components=2).fit_transform(numpy.array(embeddings))

    for post, umap_result in zip(all_posts, umap_result):
        post._x, post._y = umap_result

    art_embedding = _sentence_transformer.encode("art, beauty")
    musicality_embedding = _sentence_transformer.encode("music, melodies")
    computers_embedding = _sentence_transformer.encode(
        "programming, computers, internet"
    )

    for post in all_posts:
        post.length_normalized = len(post.content)
        post.art_relatedness = float(util.cos_sim(art_embedding, post.embeddings))
        post.music_relatedness = float(
            util.cos_sim(musicality_embedding, post.embeddings)
        )
        post.computers_relatedness = float(
            util.cos_sim(computers_embedding, post.embeddings)
        )

    max_length = max(post.length_normalized for post in all_posts)

    max_art_relatedness = max(post.art_relatedness for post in all_posts)
    max_music_relatedness = max(post.music_relatedness for post in all_posts)
    max_computer_relatedness = max(post.computers_relatedness for post in all_posts)

    for post in all_posts:
        post.art_relatedness /= max_art_relatedness
        post.music_relatedness /= max_music_relatedness
        post.computers_relatedness /= max_computer_relatedness
        post.length_normalized /= max_length

    for post in all_posts:
        post.related_posts = [
            RelatedPost(post=similar_post, similarity=post.distance_to(similar_post))
            for similar_post in sorted(
                all_posts, key=lambda post_to_sort: post_to_sort.distance_to(post)
            )
            if similar_post != post
        ]

    logger.info(
        "Sentence transformer cache hit/miss ratio: %i/%i",
        _sentence_transformer.cache_hits,
        _sentence_transformer.cache_misses,
    )

    return all_posts
