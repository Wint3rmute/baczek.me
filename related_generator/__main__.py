"""
Credit: https://flavioclesio.com/cosine-similarity-search-for-new-documents-using-scikit-learn
Source SO post: https://stackoverflow.com/questions/44862712/td-idf-find-cosine-similarity-between-new-document-and-dataset/44863365#44863365

Disclaimer: I am not a data scientist, just a random guy who wanted to make an automatic
"related posts" section generator. This script is by no means proffesional
nor comprehensive in any way, it's just a quick hack that is good enough for me.

"""
import json
from pathlib import Path

import graphviz
import nltk
import umap
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity

from .post import Post, get_all_posts


def tokenizer(text: str) -> list[str]:
    stemmer = SnowballStemmer("english")
    words = word_tokenize(text)

    return [stemmer.stem(word) for word in words]


if __name__ == "__main__":

    nltk.download("punkt")
    all_posts = get_all_posts()

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode([post.content for post in all_posts])

    umap_result = umap.UMAP().fit_transform(embeddings)

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
        transparency = f"{int(255 * post.posts_linking_to_this):02x}"
        color = "#ffffff"
        color += transparency

        relations_graph.node(
            post.title,
            color=color,
            fontcolor="white",
            xlabel="🆕" if post.recently_modified else "",
            URL="/" + post.path.with_suffix("").name,
        )

    linked_with = {post.path: [] for post in all_posts}

    for post in all_posts:
        related_posts_json_path = Path("./generated") / post.path.relative_to(
            "content"
        ).with_suffix(".json")
        related_posts_json_path.parent.mkdir(parents=True, exist_ok=True)

        related_posts_json = []

        # for post_ in all_posts:
        #     if len(set(post.tags) & set(post_.tags)) != 0:
        #         relations_graph.edge(post.title, post_.title, color="transparent")

        for post_id in post.related_post_ids:
            related_post = all_posts[post_id]

            if (
                related_post.path not in linked_with[post.path]
                and post.path not in linked_with[related_post.path]
            ):
                relations_graph.edge(post.title, related_post.title, color="white")
                linked_with[post.path].append(related_post.path)
                linked_with[related_post.path].append(post.path)

            post_link = "/" + str(
                related_post.path.relative_to("content").parent
                / related_post.path.relative_to("content").stem
            )

            related_posts_json.append({"title": related_post.title, "url": post_link})

        with open(related_posts_json_path, "w", encoding="utf-8") as relations_file:
            json.dump({"posts": related_posts_json}, relations_file)

    # Note: it actually renders to connections.svg
    relations_graph.render("./generated/connections")
