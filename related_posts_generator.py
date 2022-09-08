"""
Credit: https://flavioclesio.com/cosine-similarity-search-for-new-documents-using-scikit-learn
Source SO post: https://stackoverflow.com/questions/44862712/td-idf-find-cosine-similarity-between-new-document-and-dataset/44863365#44863365

Disclaimer: I am not a data scientist, just a random guy who wanted to make an automatic
"related posts" section generator. This script is by no means proffesional
nor comprehensive in any way, it's just a quick hack that is good enough for me.

"""
import json
import math
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import graphviz
import matplotlib.pyplot as plt
import nltk
import umap
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("punkt")


@dataclass
class Post:
    title: str
    content: str
    path: Path

    # To be filled by map generation
    x: float = 0.0
    y: float = 0.0

    related_post_ids: list[int] = field(default_factory=list)
    posts_linking_to_this: int = 0

    @classmethod
    def from_path(cls, path: Path):

        if path.suffix == ".md":

            content = subprocess.check_output(
                ["pandoc", "-f", "markdown", "-t", "plain", path.absolute()]
            ).decode()

            content_raw = path.read_text()
            title = None

            for line in content_raw.split("\n"):
                if "title: " in line:
                    title = line.replace("title: ", "").strip()

            if not title:
                raise ValueError(f"Title not found in {path}")

        elif path.suffix == ".html":
            content_raw = path.read_text()

            content = subprocess.check_output(
                f"sed 's/<nav>.*<\/nav>//' {path} | pandoc -f html -t plain -",
                shell=True,
            ).decode()
            title = path.name

        return cls(title, content, path)

    def distance_to(self, post: "Post") -> float:
        return math.sqrt((self.x - post.x) ** 2 + (self.y - post.y) ** 2)


def get_all_posts() -> list[Post]:
    all_posts = []
    all_posts_paths = Path.glob(Path("./content/"), "**/*.md")

    for post_path in all_posts_paths:
        all_posts.append(Post.from_path(post_path))

    return all_posts


def tokenizer(text: str) -> list[str]:
    stemmer = SnowballStemmer("english")
    words = word_tokenize(text)

    return [stemmer.stem(word) for word in words]


if __name__ == "__main__":
    all_posts = get_all_posts()

    # Vectorizer to convert a collection of raw documents to a matrix of TF-IDF features
    vectorizer = TfidfVectorizer(tokenizer=tokenizer)
    # vectorizer = TfidfVectorizer()

    # Learn vocabulary and idf, return term-document matrix.
    tfidf = vectorizer.fit_transform([post.content for post in all_posts])

    # Array mapping from feature integer indices to feature name
    words = vectorizer.get_feature_names_out()

    umap_result = umap.UMAP().fit_transform(tfidf)

    for post, umap_result in zip(all_posts, umap_result):
        post.x, post.y = umap_result

    print("Generating related posts...")
    for post_index, post in enumerate(all_posts):
        # We can check that using a new document text
        requested_index = post_index

        related_posts = sorted(
            all_posts, key=lambda post_to_sort: post_to_sort.distance_to(post)
        )

        related_product_indices = []
        for related_post in related_posts:
            for post_index, post_ in enumerate(all_posts):
                if related_post.title == post_.title:
                    related_product_indices.append(post_index)

        related_product_indices = [
            i for i in related_product_indices if i != requested_index
        ]

        post.related_post_ids = related_product_indices[:3]

    for post in all_posts:
        for post_id in post.related_post_ids:
            all_posts[post_id].posts_linking_to_this += 1

    max_num_of_links = max(post.posts_linking_to_this for post in all_posts)

    for post in all_posts:
        post.posts_linking_to_this /= max_num_of_links

    relations_graph = graphviz.Graph(
        comment="All Relations",
        graph_attr={"bgcolor": "transparent", "overlap": "false"},
        format="svg",
        node_attr={"shape": "box"},
        engine="neato",
    )

    for post in all_posts:
        color = f"#ffffff{int(255 * post.posts_linking_to_this):02x}"
        relations_graph.node(
            post.title,
            color=color,
            fontcolor="white",
            URL="/" + post.path.with_suffix("").name,
        )

    for post in all_posts:
        related_posts_json_path = Path("./generated") / post.path.relative_to(
            "content"
        ).with_suffix(".json")
        related_posts_json_path.parent.mkdir(parents=True, exist_ok=True)

        related_posts_json = []

        for post_id in post.related_post_ids:
            related_post = all_posts[post_id]
            relations_graph.edge(post.title, related_post.title, color="white")

            post_link = "/" + str(
                related_post.path.relative_to("content").parent
                / related_post.path.relative_to("content").stem
            )

            related_posts_json.append({"title": related_post.title, "url": post_link})

        with open(related_posts_json_path, "w", encoding="utf-8") as relations_file:
            json.dump({"posts": related_posts_json}, relations_file)

    # Note: it actually renders to connections.svg
    relations_graph.render("./generated/connections")
