---
title: Decentralisation
tags: programming
---

As many other people who run their own websites (and often other
web infrastructure), I'm interested in keeping the internet
diverse and decentralised.

<!-- ## Making the internet interesting again -->

{{image (src="/computer_poster.jpg" small=true title="How it feels to browse the Small Web")}}

Check out my [bookmarks](/bookmarks)!

## Decentralised/self-hosted/privacy-first online services

I'm running self-hosted online services. They are public, you can
use them too :)

- [Invidious](https://invidious.baczek.me), an alternate YouTube frontend

- [SearX](https://searx.baczek.me), a meta-search engine

- [LibreY](https://librey.baczek.me), another meta-search engine

- [Libreddit](https://libreddit.baczek.me), alternative Reddit frontend


I also recommend the following services for private use:

- [NextCloud](https://nextcloud.com/)

- [Matrix](https://github.com/matrix-org/synapse/) 


>some random thoughts on search - [registry-based search engine manifesto](/search-registry-manifesto)


## Notes on self-hosting, suggested software

1. Monitor the metrics of every service you've hosting (Prometheus)
2. Visualise your metrics (Grafana)
3. Ping everything from time to time (Blackbox exporter)
4. Setup notifications when a service goes down
5. Automate everything from the start, you won't regret it
6. As your infrastructure (and knowledge) grows, you will eventually need *infrastructure as code*
    - Or even better, just use [NixOs](/nixos)
