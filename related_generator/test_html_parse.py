from pathlib import Path

from .post import Post

all_posts_paths = Path.glob(Path("/home/wint3rmute/code/misc/oscean/site"), "*.html")


def all_paths_generator():
    for post_path in all_posts_paths:
        yield post_path


for path in all_paths_generator():
    p = Post.from_path(Path(path))
    to_trim = p.content.rfind("Incoming:")

    if to_trim != -1:
        p.content = p.content[to_trim:]
    else:
        print("Not trimming", p.title)
        print(p.content[-100:])
        print("==========")
