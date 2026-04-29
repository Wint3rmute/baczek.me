import json
import logging
from datetime import datetime
from pathlib import Path

from exocortex.page import Post

logger = logging.getLogger(__name__)


def generate_recently_updated(all_posts: list[Post]):
    recent_updates = [
        {"title": post.title, "url": post.link}
        for post in all_posts
        if post.recently_modified
    ]

    logger.info("Recently updated JSON: %r", recent_updates)
    Path("./generated/recently_updated.json").write_text(json.dumps(recent_updates))


def write_build_date():
    logger.info("Writing build date...")
    Path("./generated/build_date.txt").write_text(
        datetime.now().strftime("%d/%m/%y %H:%M")
    )
