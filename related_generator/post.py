import math
import markdown
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from bs4 import BeautifulSoup


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
            content_raw = path.read_text()
            # No easy markdown to text convertsion available at the moment :/
            html = markdown.markdown(content_raw)
            html_tree = BeautifulSoup(html, features="html.parser")
            content = html_tree.text

            title = None

            for line in content_raw.split("\n"):
                if "title: " in line:
                    title = line.replace("title: ", "").strip()

            if not title:
                raise ValueError(f"Title not found in {path}")

        elif path.suffix == ".html":
            content_raw = path.read_text()
            html_tree = BeautifulSoup(content_raw, features="html.parser")
            html_tree.nav.decompose()
            content = html_tree.text.replace("\n", "")

            title = path.name

            to_trim = content.rfind("Incoming:")
            if to_trim != -1:
                content = content[to_trim:]
            # else:
            #     print("No Incoming")
            #     print(content)

        return cls(title, content, path)

    def distance_to(self, post: "Post") -> float:
        return math.sqrt((self.x - post.x) ** 2 + (self.y - post.y) ** 2)


def get_all_posts() -> list[Post]:
    all_posts = []
    all_posts_paths = Path.glob(Path("./content/"), "**/*.md")

    for post_path in all_posts_paths:
        all_posts.append(Post.from_path(post_path))

    return all_posts
