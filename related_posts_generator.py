"""
Credit: https://flavioclesio.com/cosine-similarity-search-for-new-documents-using-scikit-learn
Source SO post: https://stackoverflow.com/questions/44862712/td-idf-find-cosine-similarity-between-new-document-and-dataset/44863365#44863365

Disclaimer: I am not a data scientist, just a random guy who
wanted to make an automatic "related posts" section generator

"""
import json
from dataclasses import dataclass
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

all_posts_paths = Path.glob(Path("./content/"), "**/*.md")


@dataclass
class Post:
    title: str
    content: str
    path: Path

    @classmethod
    def from_path(cls, path: Path):
        content = path.read_text()

        title = None
        for line in content.split("\n"):
            if "title: " in line:
                title = line.replace("title: ", "").strip()

        if not title:
            raise ValueError("Title not found in %s", path)

        return cls(title, content, path)


all_posts = []

for post_path in all_posts_paths:
    all_posts.append(Post.from_path(post_path))

# Vectorizer to convert a collection of raw documents to a matrix of TF-IDF features
vectorizer = TfidfVectorizer()

# Learn vocabulary and idf, return term-document matrix.
tfidf = vectorizer.fit_transform([post.content for post in all_posts])

# Array mapping from feature integer indices to feature name
words = vectorizer.get_feature_names_out()

# Compute cosine similarity between samples in X and Y.
similarity_matrix = cosine_similarity(tfidf, tfidf)


visualisation_str = "digraph {  node [shape=box];\n "

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

    related_product_indices = related_product_indices[:3]

    related_posts_json = Path("./generated") / post.path.relative_to(
        "content"
    ).with_suffix(".json")

    related_posts_json.parent.mkdir(parents=True, exist_ok=True)
    with open(related_posts_json, "w") as related_links_json:
        related_posts = []
        for post_id in related_product_indices:
            related_post = all_posts[post_id]
            post_link = (
                related_post.path.relative_to("content").parent
                / related_post.path.relative_to("content").stem
            )
            related_posts.append({"title": related_post.title, "url": "/" + str(post_link)})
            visualisation_str += f"\"{post.title}\" -> \"{related_post.title}\"\n"
            visualisation_str += f"\"{related_post.title}\"[URL=\"/{post_link}\"]\n"

        json.dump({"posts": related_posts}, related_links_json)

visualisation_str += "\n}"
with open("generated/connections.dot", "w") as graph_file:
    graph_file.write(visualisation_str)

