import json
import logging
import textwrap
from pathlib import Path

import graphviz

from exocortex.page import Post

logger = logging.getLogger(__name__)

ACCENT_COLOR = "#82AAFF"
UMAP_POSITION_TO_GRAPHVIZ_MULTIPLIER = 0.40


def make_node(graph: graphviz.Graph, post: Post, accent_style: bool = False):
    if accent_style:
        color = ACCENT_COLOR
    else:
        color = "#ffffff"
        transparency = f"{int(255 * post.weirdness):02x}"
        color += transparency

    xlabel = ""
    if post.recently_modified:
        xlabel = "!"

    graph.node(
        post.title,
        # label="< <B>" + graphviz.nohtml(post.title) + "</B> >",
        label="\n".join(textwrap.wrap(post.title, width=16)),
        color=color,
        fillcolor="#263238",
        style="filled",
        fontcolor=ACCENT_COLOR if accent_style else "white",
        penwidth="2.0" if accent_style else "1.0",
        xlabel=xlabel,
        URL="/" + post.path.with_suffix("").name,
        pos=f"{post.x * UMAP_POSITION_TO_GRAPHVIZ_MULTIPLIER},{post.y * UMAP_POSITION_TO_GRAPHVIZ_MULTIPLIER}!",
    )


def render_maps(all_posts: list[Post]):
    logger.info("Rendering maps...")

    graph = graphviz.Graph(
        comment="All Relations",
        graph_attr={
            "bgcolor": "transparent",
            "overlap": "false",
            "outputorder": "edgesfirst",
        },
        format="svg",
        node_attr={"shape": "box", "nodesep": "0.55"},
        engine="neato",
    )

    existing_connections: list[set[Post, Post]] = []

    for post in all_posts:
        make_node(graph, post)

        related_posts = [
            similiar_post
            for similiar_post in sorted(
                all_posts, key=lambda post_to_sort: post_to_sort.distance_to(post)
            )
            if similiar_post.path != post.path
        ]

        related_posts_json_path = Path("./generated") / post.path.relative_to(
            "content"
        ).with_suffix(".json")
        related_posts_json_path.parent.mkdir(parents=True, exist_ok=True)

        with open(related_posts_json_path, "w", encoding="utf-8") as relations_file:
            json.dump(
                {
                    "posts": [
                        {"title": related_post.title, "url": related_post.link}
                        for related_post in related_posts[:2]
                    ]
                },
                relations_file,
            )

        connections_created = 0
        for related in related_posts:
            if {post, related} not in existing_connections:
                graph.edge(
                    post.title,
                    related.title,
                    color="white" if connections_created == 0 else "gray",
                )
                existing_connections.append({post, related})
                connections_created += 1

            if connections_created > 1:
                break

    # Note: it actually renders to connections.svg
    graph.render("./generated/connections")

    for current_post in all_posts:
        graph = graphviz.Graph(
            comment="Relations for node",
            graph_attr={
                "bgcolor": "transparent",
                "overlap": "false",
                "outputorder": "edgesfirst",
            },
            format="svg",
            node_attr={"shape": "box", "nodesep": "0.55"},
            engine="neato",
        )

        posts_nearby = sorted(all_posts, key=lambda p: p.distance_to(current_post))

        nodes_in_graph = {current_post}
        make_node(graph, current_post, accent_style=True)

        for post in posts_nearby[1:6]:
            logger.debug(" Making node %s", post.title)
            nodes_in_graph.add(post)
            make_node(graph, post, accent_style=False)

        for connection in existing_connections:
            if len(connection & nodes_in_graph) == 2:
                node_1 = list(connection)[0]
                node_2 = list(connection)[1]

                logger.debug("Linking %s with %s", node_1.title, node_2.title)
                graph.edge(
                    node_1.title,
                    node_2.title,
                    color="white" if (id(node_1) // 10) % 2 else "gray",
                    # color="white" if target in [ post.post for post in post.related_posts][:1] else "gray",
                )

        related_posts_svg_path = Path("./generated") / current_post.path.relative_to(
            "content"
        ).with_suffix("")
        related_posts_svg_path.parent.mkdir(parents=True, exist_ok=True)
        graph.render(related_posts_svg_path)
