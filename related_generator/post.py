import math
import subprocess
import warnings
from dataclasses import dataclass, field
from pathlib import Path

import markdown
from bs4 import BeautifulSoup


def was_recently_modified(file_path: Path) -> bool:
    recently_modified_files = subprocess.check_output(
        "git log --pretty=format: --name-only | grep '.md' | awk '!seen[$0]++' | head -n 5",
        shell=True,
    ).decode()

    for file in recently_modified_files.split("\n"):
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


def extract_tags(file_path: Path, content: str) -> list[str]:
    tags = []

    for line in content.split("\n"):
        if line.startswith("tags: "):
            tags = line.replace("tags: ", "").split(",")
            tags = [tag.strip() for tag in tags]

    if len(tags) == 0:
        warnings.warn(f"No tags defined for {file_path}")

    return tags


@dataclass
class Post:
    title: str
    content: str
    path: Path
    recently_modified: bool
    tags: list[str] = field(default_factory=list)

    # To be filled by map generation
    x: float = 0.0
    y: float = 0.0

    related_post_ids: list[int] = field(default_factory=list)
    posts_linking_to_this: int = 0

    @classmethod
    def from_path(cls, path: Path):

        if path.suffix == ".md":
            content_raw = path.read_text()
            # No easy markdown to text convertsion available at the moment :/
            html = markdown.markdown(content_raw)
            html_tree = BeautifulSoup(html, features="html.parser")
            content = html_tree.text

            title = extract_title(path, content_raw)
            tags = extract_tags(path, content_raw)

        elif path.suffix == ".html":
            content_raw = path.read_text()
            html_tree = BeautifulSoup(content_raw, features="html.parser")
            html_tree.nav.decompose()
            content = html_tree.text.replace("\n", "")
            tags = []

            title = path.name

            to_trim = content.rfind("Incoming:")
            if to_trim != -1:
                content = content[to_trim:]
            # else:
            #     print("No Incoming")
            #     print(content)

        return cls(title, content, path, was_recently_modified(path), tags)

    def distance_to(self, post: "Post") -> float:
        return math.sqrt((self.x - post.x) ** 2 + (self.y - post.y) ** 2)


def get_all_posts() -> list[Post]:
    all_posts = []
    all_posts_paths = Path.glob(Path("./content/"), "**/*.md")

    for post_path in all_posts_paths:
        all_posts.append(Post.from_path(post_path))

    return all_posts
