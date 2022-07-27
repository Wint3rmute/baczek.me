---
created: 2022-06-26T22:51:04+02:00
modified: 2022-07-27T17:48:13+02:00
title: Daily open-source software guide
---

I've found that lots of people are writing extensive lists of tools they use to get things done, whether open source or not. I've decided to do it in a slightly different way - by imagining a day of my life, when I'm using various open source tools to do things that most of the people use proprietary software for.

I believe that using FOSS software results in a more healthy lifestyle
and approach to technology, as the software will not try to manipulate you
into consuming more content.
The only thing driving you while using free & open source software is
you own curiosity and will.

# Waking up

Not a lot of software here, mostly hardware like the fridge and some cutlery. I've decided to leave this phase in case I come up with some software examples in the future. 

# Transit to work/University

>You can always **read a book instead**. 
>But I get it, you're here for the software,
>so here we go:

Instead of scrolling through social media, use an
[RSS reader](https://f-droid.org/en/packages/com.nononsenseapps.feeder/)
and find some interesting blogs to follow. I also recommend keeping a list
of webrings or other pages that are run by people or
small organisations, not companies/corporations.

# Work/University

## Searching for information on the internet

Use [DuckDuckGo](duckduckgo.com/) or [SearX](https://searx.space/). They won't track you or suggest any targeted content.

## Creating a slideshow

- The quick way: write them in markdown and use [pandoc](https://pandoc.org/demos.html) to convert them into a presentation (I recommend using the revealJS slide show)
- The longer but more customizable way: use beamer (try [Metropolis Theme](https://www.overleaf.com/latex/templates/metropolis-beamer-theme/qzyvdhrntfmrfor) for a sleek, minimal look)

## A need for something Excel-like (and spreadsheets in general) 

- Just use the python interpreter (or `ipython` if you wanna get fancy) for quick calculations. 
- Try [Jupyter Lab](https://jupyter.org/) if you're working on something bigger

# Time spent at home

## Internet Surfing (the old school way)

[Wiby](http://wiby.me/) is a search engine, which indexes only minimalist websites.
It's great for finding hand-crafted sites and old gems from before the FAANG age.

![Wiby main page screenshot](/wiby.jpg)

[Merveilles Webring Search Engine](https://lieu.cblgh.org/) - indexes the sites made by people from [Merveilles](merveilles.town).


>I highly recommend searching for niche movies/music/art in those web engines,
>as they will lead you to more in-depth articles than Google/Bing/etc.

## VPN/Networking

- Get a VPS and install [WireGuard](https://www.wireguard.com/). It's definitely more work than using something like Tailscale or ZerotierOne, but it will pay off in networking & server administration skills.

## Cloud drive

- Nextcloud is surprisingly easy to setup and maintain

## Taking Notes

- GitJournal works wonders as a markdown-based notes tool that you can integrate with your existing git workflow
