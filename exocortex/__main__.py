"""
Parses all posts as text and creates a "semantic map", grouping
similar posts together on a 2D plane. Basically:

1. Sentence embeddings
2. Umap
3. Some semi-random links between nodes to make it look smarter than it actually is
4. Graphviz to SVG
5. Display SVG on the site

This notebook also contains some other small utilities used in the site build process,
but their importance is negligible therefore I do not document them all.

---

Notes on the previous version from the preGPT era:

Credit: https://flavioclesio.com/cosine-similarity-search-for-new-documents-using-scikit-learn
Source SO post: https://stackoverflow.com/questions/44862712/td-idf-find-cosine-similarity-between-new-document-and-dataset/44863365#44863365

Disclaimer: I am not a data scientist, just a random guy who wanted to make an automatic
"related posts" section generator. This script is by no means proffesional
nor comprehensive in any way, it's just a quick hack that is good enough for me.
"""

import logging

from exocortex.map import render_maps
from exocortex.misc import generate_recently_updated, write_build_date
from exocortex.page import get_all_posts
from exocortex.rss import generate_rss_feed

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

all_posts = get_all_posts()

render_maps(all_posts)
generate_recently_updated(all_posts)
generate_rss_feed()
write_build_date()
