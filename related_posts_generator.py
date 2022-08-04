"""
Credit: https://flavioclesio.com/cosine-similarity-search-for-new-documents-using-scikit-learn
Source SO post: https://stackoverflow.com/questions/44862712/td-idf-find-cosine-similarity-between-new-document-and-dataset/44863365#44863365

Disclaimer: I am not a data scientist, just a random guy who wanted to make an automatic
"related posts" section generator. This script is by no means proffesional
nor comprehensive in any way, it's just a quick hack that is good enough for me.

"""
import json
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import graphviz
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class Post:
    title: str
    content: str
    path: Path

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
                f"sed 's/<nav>.*<\/nav>//' {path} | pandoc -f html -t plain -", shell=True,
            ).decode()
            title = path.name

        return cls(title, content, path)


def get_all_posts() -> list[Post]:
    all_posts = []
    all_posts_paths = Path.glob(Path("./content/"), "**/*.md")

    for post_path in all_posts_paths:
        all_posts.append(Post.from_path(post_path))

    return all_posts


if __name__ == "__main__":
    all_posts = get_all_posts()

    # Vectorizer to convert a collection of raw documents to a matrix of TF-IDF features
    vectorizer = TfidfVectorizer()

    # Learn vocabulary and idf, return term-document matrix.
    tfidf = vectorizer.fit_transform([post.content for post in all_posts])

    tsne_result = TSNE(
        n_components=2, learning_rate="auto", init="random"
    ).fit_transform(tfidf)

    # Array mapping from feature integer indices to feature name
    words = vectorizer.get_feature_names_out()

    # Compute cosine similarity between samples in X and Y.
    similarity_matrix = cosine_similarity(tfidf, tfidf)

    print("Generating related posts...")
    for post_index, post in enumerate(all_posts):
        # We can check that using a new document text
        requested_index = post_index
        query = all_posts[requested_index].content  # "software"
        print("-", all_posts[requested_index].title)

        # Instead of using fit_transform, you need to first fit
        # the new document to the TFIDF matrix corpus like this:
        queryTFIDF = TfidfVectorizer().fit([post.content for post in all_posts])

        # Now we can 'transform' this vector into that matrix shape by using the transform function:
        queryTFIDF = queryTFIDF.transform([query])

        # As we transformed our query in a tfidf object
        # we can calculate the cosine similarity in comparison with
        # our pevious corpora
        cosine_similarities = cosine_similarity(queryTFIDF, tfidf).flatten()

        # Get most similar jobs based on next text
        related_product_indices = cosine_similarities.argsort()[:-11:-1]

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

    relations_graph = graphviz.Digraph(
        comment="All Relations",
        graph_attr={"bgcolor": "transparent"},
        format="svg",
        node_attr={"shape": "box"},
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
