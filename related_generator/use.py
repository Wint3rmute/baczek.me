# @title Load the Universal Sentence Encoder's TF Hub module
import os
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
import tensorflow_hub as hub
from absl import logging

from .post import get_all_posts

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"  # @param ["https://tfhub.dev/google/universal-sentence-encoder/4", "https://tfhub.dev/google/universal-sentence-encoder-large/5"]
model = hub.load(module_url)
print("module %s loaded" % module_url)


def embed(input):
    return model(input)


# @title Compute a representation for each message, showing various lengths supported.
# word = "Elephant"
# sentence = "I am a sentence for which I would like to get its embedding."
# paragraph = (
#     "Universal Sentence Encoder embeddings also support short paragraphs. "
#     "There is no hard limit on how long the paragraph is. Roughly, the longer "
#     "the more 'diluted' the embedding will be."
# )


def plot_similarity(labels, features, rotation):
    corr = np.inner(features, features)
    plt.figure(figsize=(10, 5))
    sns.set(font_scale=0.1)
    g = sns.heatmap(
        corr, xticklabels=labels, yticklabels=labels, vmin=0, vmax=1, cmap="YlOrRd"
    )
    g.set_xticklabels(labels, rotation=rotation)
    g.set_title("Semantic Textual Similarity")
    # g.show()
    # sns.plt.show()
    # __import__("pdb").set_trace()
    plt.savefig("plot.png", dpi=300)


def run_and_plot(messages, titles):
    message_embeddings_ = embed(messages)
    plot_similarity(titles, message_embeddings_, 90)


if __name__ == "__main__":
    all_posts = get_all_posts()
    messages = [post.content for post in all_posts]
    titles = [post.title for post in all_posts]

    # Reduce logging output.
    logging.set_verbosity(logging.ERROR)

    message_embeddings = embed(messages)

    for i, message_embedding in enumerate(np.array(message_embeddings).tolist()):
        print("Message: {}".format(messages[i]))
        print("Embedding size: {}".format(len(message_embedding)))
        message_embedding_snippet = ", ".join((str(x) for x in message_embedding[:3]))
        print("Embedding: [{}, ...]\n".format(message_embedding_snippet))

    run_and_plot(messages, titles)
