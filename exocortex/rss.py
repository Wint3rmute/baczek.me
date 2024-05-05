import logging
from datetime import datetime

from git import Repo

logger = logging.getLogger(__name__)

ATOM_FEED_HEAD = """
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">

<title>Baczek.me Devlog</title>
<link href="https://baczek.me/"/>
<updated>2003-12-13T18:30:02Z</updated>
<author>
<name>Mateusz Bączek</name>
</author>
<id>https://baczek.me/</id>
"""

ATOM_FEED_TAIL = """ 
</feed>
"""

DEVLOG_URL = "https://baczek.me/now"


def generate_entry(link: str, updated: datetime, commit_hash: str) -> str:
    return f"""
      <entry>
        <title>{updated.strftime('%d.%m.%Y')} Devlog update</title>
        <link href="{link}"/>
        <updated>{updated.isoformat()}</updated>
        <summary>DevLog available at {link}</summary>
        <id>https://baczek.me/now#f{commit_hash}</id>
      </entry>
  """


def generate_rss_feed():
    with open("./static/atom.xml", "w") as feed_file:
        repo = Repo("./")
        devlog_changes = list(
            repo.iter_commits(all=True, paths="./content/now.md")
        )  # Gets the last 10 commits from all branches.
        devlog_changes.reverse()

        feed_file.write(ATOM_FEED_HEAD)

        for commit in devlog_changes:
            logger.debug("Generating RSS entry for %s", commit.committed_datetime)
            feed_file.write(
                generate_entry(DEVLOG_URL, commit.committed_datetime, commit.hexsha)
            )

        feed_file.write(ATOM_FEED_TAIL)

    logger.info("RSS feed generated")
