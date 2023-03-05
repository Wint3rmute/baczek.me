import gensim.downloader as api
import numpy as np
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from scipy import spatial

from .post import get_all_posts

model = api.load(
    "glove-wiki-gigaword-50"
)  # choose from multiple models https://github.com/RaRe-Technologies/gensim-data


def preprocess(text: str) -> list[str]:
    stemmer = SnowballStemmer("english")
    words = word_tokenize(text)

    return [stemmer.stem(word) for word in words]


# def preprocess(s) -> list[str]:
#     return [i.lower() for i in s.split()]


def get_vector(s):
    return np.sum(np.array([model[i] for i in preprocess(s) if i in model]), axis=0)


if __name__ == "__main__":
    posts = get_all_posts()

    s0 = posts[0].content
    s1 = posts[1].content
    s2 = posts[2].content
    s3 = posts[3].content

    t0 = posts[0]
    t1 = posts[1]
    t2 = posts[2]
    t3 = posts[3]

    print(
        f"{t0.title} vs {t1.title} ->",
        1 - spatial.distance.cosine(get_vector(s0), get_vector(s1)),
    )
    print(
        f"{t0.title} vs {t2.title} ->",
        1 - spatial.distance.cosine(get_vector(s0), get_vector(s2)),
    )
    print(
        f"{t0.title} vs {t3.title} ->",
        1 - spatial.distance.cosine(get_vector(s0), get_vector(s3)),
    )
