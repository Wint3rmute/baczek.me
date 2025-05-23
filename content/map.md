---
title: Map
tags: journal, generative, programming
---

{{svg (src="generated/connections.svg")}}

<center>
You can click on each node, they are links!
</center>

---

This is an automatically generated graph containing all pages on my website,
along with the [connections](https://en.m.wikipedia.org/wiki/Intertwingularity)
calculated using sentence embeddings. If you're interested, you can read the
[source code](https://github.com/Wint3rmute/baczek.me/blob/main/exocortex).


## How is this thing generated?

### Explained non-technically

1. Using an AI-esque tool, I'm generating a mathematical representation of what
   each page on my site contains, in terms of contents
2. I'm laying out each page on a graph, so that it is placed close to pages
   with similar contents and far away from pages with different contents. E.x.
   programming-related stuff will be grouped together, far away from something
   travel-related.
3. I'm drawing links between pages which are the closest. This also generates
   the "related posts" section at the bottom of each page. The drawn links only
   serve aesthetic purposes.
4. Posts are colored depending on their relatedness to 3 topics:
    - More red: art-related
    - More green: computers-related
    - More blue: music-related
    - I'm working on better coloring algorithms based on various gradients

### The gory technical details

1. All of the posts are fed through an embeddings generator, I'm using the
   [Sentence Transformers](https://www.sbert.net/) Python library.
2. The embeddings are passed to [UMAP](https://arxiv.org/abs/1802.03426), a
   dimensionality reduction algorithm, which takes in multi-dimensional
   embeddings and projects it down to a 2D representation, which can be drawn
   as a graph. The projection is done so that the high-level "structure" of the
   data is preserved (at least that's what the UMAP paper states, I'm not data
   scientist to argue with the experts).
3. I'm connecting each post with its top 2 nearest posts (using more clutters
   up the map).
4. Coloring is done via calculating cosine similarity between the post content
   embeddings and embeddings of simple tag-based sentences, such as *"music,
   melodies"* or *"art, beauty"*. Currently the gradient is dead-simple,
   similarity directly affects the R/G/B channel.
5. `graphviz` renders the graphs and outputs them as SVGs.

A much better description of a similiar idea on [Simon Willison's
blog](https://simonwillison.net/2023/Oct/23/embeddings/).

## Future plans

1. Make this thing look more "map-alike", whatever that might mean.
2. Experiment with text clusterisation & dimensionality reduction algorithms,
such as:
    - tSNE
    - K-means clustering
    - UMAP
    - Latent Dirichlet allocation
    - DBSCAN
3. ~~Add #tags.~~ Automatically assign posts to categories with cosine distances.
4. Introduce color-coding and other visual markers, allowing viewers to make
sense of the data based on different metrics:
    - Post tags
    - Links to/from other posts
    - Links outside (to the *netsphere*)
    - Other connections generated by NLP
5. Check out [KagiSearch/vectordb](https://github.com/kagisearch/vectordb)
6. [Color gradients with Python](https://bsouthga.dev/posts/color-gradients-with-python)
7. [Circos](https://circos.ca/)
