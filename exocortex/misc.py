import json
import logging
from datetime import datetime

from exocortex.page import Post

logger = logging.getLogger(__name__)


def generate_recently_updated(all_posts: list[Post]):
    recent_updates = [
        {"title": post.title, "url": post.link}
        for post in all_posts
        if post.recently_modified
    ]

    with open("./generated/recently_updated.json", "w") as recent_updates_file:
        logger.info("Recently updated JSON: %r", recent_updates)
        json.dump(recent_updates, recent_updates_file)


def write_build_date():
    logger.info("Writing build date...")
    with open("./generated/build_date.txt", "w") as build_date:
        build_date.write(datetime.strftime(datetime.now(), "%d/%m/%y %H:%M"))
