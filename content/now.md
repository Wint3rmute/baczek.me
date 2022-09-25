---
title: 2022's Devlog
---

```
25.08
```

Experimenting with wavetable synthesis. I've managed to hack it into [nosna](https://github.com/Wint3rmute/nosna) and sampled my Minilogue, just to have some "homemade" wavetables. It's way more entertaining than coding an FM synthesiser, you can get a lot of interesting timbres without having to play around with operator ratios & envelopes. This "happy accidents" workflow is more funny and rewarding. On the other hand, it mostly boils down to the samples you're using to build the wavetables. 

>Listening:<br>
>Rosa Walton - I Really Want to Say at Your House


```
24.08
```

If someone had told me a year ago that there would be an anime made by Studio Trigger, in collaboration with a Polish game development company, featuring some of the most known Polish artists in its soundtrack, I wouldn't be able to stop myself from laughing at such an idea. And yet, here we are.

The feeling's magical. Thank you, CD Project Red! 

>Watching:<br>
>Cyberpunk: Edgerunners
><br>
>Listening:<br>
>Ben Bohmer - In Memoriam


```
21.08
```

Listened to a part of [Lex Fridman Podcast](https://youtu.be/VguG_y05Xe8) about [Rule 30](https://en.wikipedia.org/wiki/Rule_30).
I was familiar with cellular automatas, but only with ones that operate on 2D arrays. Using
a single dimension for the automata and visualising changes over time was something new to me.

After taking a quick dive into Wikipedia, I found [Rule 184](https://en.wikipedia.org/wiki/Rule_184). 
I liked the generated shapes, so I've experimented a bit with `python` and `imagemagick`:

{{image (src="/rule_184/rule184_1.jpg" title="The same pattern, rotated 4 times and overlayed")}}
{{image (src="/rule_184/rule184_3.jpg" title="Randomly generating, rotating and overlaying patterns")}}

That's one step closer to becoming a generative artist, I guess :)


```
18.08
```

{{image (src="/war_games.jpg" title="")}}

>Watching:<br>
>Paprika (2nd rewatch)<br>
>WarGames


```
17.09
```

Learning Kafka! 


>Music:<br>
>Brian Eno - There Were Bells<br>
>Watching:<br>
>Dredd (2012)<br>

```
05.09
```

Compiled a sample Rust application to Android using [Macroquad](https://macroquad.rs/).
It all worked out of the box, without any problems. Makes me excited, as I'll
probably be able to work on my portable groovebox, all in Rust. I just
need to hack together some way to get custom audio sources into Macroquad
or use some other library to do the low-level heavy-lifting for me.

Exploring ideas related with [physical modeling](https://ccrma.stanford.edu/~jos/pasp/).

>Music:<br>
>Coldplay - Christmas Lights<br>
><br>
>Watching:<br>
>Wes Anderson - Fantascic Mr Fox<br>
>Ari Aster - Hereditary<br>
>David Lynch - Mulholland Drive<br>


```
31.08
```

>Music:<br>
>Ben Bohmer - Begin Again
><br>
>Watching:<br>
>FLCL


```
27.08
```

Started hosting an [Invidious](https://invidious.io/) instance at [invidious.baczek.me](https://invidious.baczek.me/).
It provides a way better experience than YouTube, especially when listening to podcasts. I am not interrupted every ~30 minutes with 
ads that I have to manually skip for them to stop playing.

Wrote a proof of concept [custom oscillator](https://github.com/Wint3rmute/minilogue-xd-karplus-strong)
for my [Minilogue](https://www.korg.com/us/products/synthesizers/minilogue_xd/).

>Music:<br>
>Baasch - Brokat<br>


```
24.08
```

My time gets eaten away by work as we're finishing a big project.
Hopefully I'll rest in the upcoming month and prepare some materials
to submit the idea for my master's thesis to the uni.

>Music:<br>
>Agnes Obel - Riverside<br>

Went to Agnes Obel's concert in my hometown.
I'm really starting to enjoy live music :)


```
16.08
```

Experimenting on visualisations, pairing UMAP with GraphViz. 
This is an in-between state of post visualisation, I've rewritten
the similiarity calculation code but left the GraphViz visualisation part.

The resulting graph is still very far from anything I'd call decent.
I'm positive that the steps, while small, are leading in the right direction.

Here's another not-so-bad-looking graph generated during development:
![UMAP + Graphviz text visualisation example graph](/umap_plus_graphviz_my_page.jpg)

---

**Late night update:** Took a while to read more of *Graphviz* documentation. Turns out that they have a special
layout engine called *neato* for drawing non-directed graphs. I tried it and I'm
amazed, it works wonderfully!

![UMAP + Graphviz + Neato text visualisation example graph](/neato_visualisation.jpg)


>Music:<br>
>Depeche Mode - But Not Tonight, Live


```
14.08
```

Configured *Prometheus* and *Grafana* for VPS monitoring. Since it is facing the public site
of the internet with my website and SearX instance (see yesterday's entry), I should be collecting
performance & health metrics. I will probably host [Invidious](https://invidious.io/) in the future as well.

{{image (src="/vps_monitoring.png" title="Grafana dashboard used for monitoring my VPS. I like graphs, they're calming.")}}

Found out about the [512kb.club](https://github.com/kevquirk/512kb.club), I'm considering joining
them when my website will look less like a portfolio and more like a exocortex/idea sharing space.
First 512kb, then hopefully the [XXIIVV webring](https://webring.xxiivv.com) :)

---

(At night) Redesigned the index page and updated the main website template.
Happy to see that I'm getting along pretty well with CSS. Never saw much
logic in it but I'm starting to understand it, at least for my simple needs.

>Music:<br>
>Orchestral Manoeuvres in the Dark - Souvenir<br>
>Ben Bohmer - Beyond Beliefs<br>
>Strawberry Guy - F Song (slowed down to 80% in audacity)


```
13.08
```

Started hosting a [SearXNG](https://searx.github.io/searx/) instance at [searx.baczek.me](https://searx.baczek.me).
I encourage you to [host one yourself](https://github.com/searxng/searxng-docker) if you're interested
in decentralisation of the internet.

I've learned a bit more about website security hardening when setting up the instance. If you're planning to proxy
search queries through a self-hosted meta-search engine instance (lots of web security lingo here), you better
make sure that you won't be leaking any information regarding the queries that the users are making.
Otherwise, you're **no better than FAANG** :)

From reading the
issues at [Searx-instance](https://github.com/searxng/searx-instances) I've learned about 2 new
tools for checking website security. Try them out if you're hosting anything yourself:

- [cryptcheck.fr](https://cryptcheck.fr/)
- [observatory.mozilla.org](https://observatory.mozilla.org/)

---

End of the day update: the instance has been accepted by SearX maintainers and is now visible at [searx.space](https://searx.space).

>Music:<br>
>Taeko Onuki: 4:00A.M.<br>
>Beardyman: Shelter me from the rain


```
04.08
```

Added stemming to the algorithm generating related posts, I'm seeing a lot of improvement!

{{image (src="/xxiivv_umap_stemming.jpg" title="After stemming, clusters are clearly visible, even when fully unzoomed.
I am still testing on XXIIVV blog contents, as it has lots and lots of posts.") }}


```
03.08
```

Experimenting with [UMAP](https://umap-learn.readthedocs.io/en/latest/) for [related posts exploration](/website-map).
I'm testing it on [XXIIVV](http://xxiivv.com/) again, but this time **without cheating**, preprocessing removes
the `<nav>` blocks containing links to other pages, the algorithm works only with each page's content. Results are promising:

{{image (src="/xxiivv_umap.jpg" title="Portion of the projection generated by UMAP.") }}

>Music:<br>
>Al Steward - Year of the Cat


```
01.08
```

Cleaned up the site deployment code, moved the docker image to Fedora + Python3.9 (3.10 does not yet have wheels for `sklearn` and there are some problems with numpy compatibility). I'm now ready to test UMAP for [site map](/website-map) generation :)

>Music:<br>
>Harmonia & Eno '76 - Welcome<br>
>Ben Bohmer - Fade to Blue

```
29.07
```

Exploring ideas related with sound fingerprinting and song similarity calculation. *Computer Vision for Music Identification* is the most interesting paper I've found so far. Even in such niche use cases, [Arch Linux repos still deliver](https://archlinux.org/packages/extra/x86_64/chromaprint/). 

{{image (src="/olsztyn-festival-logo.jpg" title="Logo of a music/art festival in Olsztyn. `ulotne` is a play on words, meaning both something passing, transitory, delicate and something that is capable of flying") }}

Implemented site auto-deployment with github webhooks. 

```
26.07 
```

Busy sailing with friends at Mazury, a region of Poland with lots of nice lakes. Sailing helps a lot when taking a break from technology as I don't get bored watching the waves, boat and landscapes around. 

I finally have some time to dig through The Rust Book now :)

{{image (src="/sailing_mazury.jpg", title="Mazury, Poland")}}

```
19.07 
```

Implemented the first prototype of automated mind mapping, using word vectorisation
and out-of-the-box graphing algorithms. I'm gonna need more content on the site
for this feature to become useful.

It looks promising when run on blogs with lots of entries:

![text vectorisation example graph](/xxiivv_text_vectorisation_example.jpg)
*Posts on [XXIIVV](http://xxiivv.com/), plugged into the visualisation script*

*Note:* honestly, I'm cheating in this example. Blog's author, [Devine](https://wiki.xxiivv.com/site/devine_lu_linvega.html),
is writing all the links to related pages manually. Because of this, text vectorisation has
no problems with connecting the dots :) On the other hand, this experiment made me more confident
that semi-automatic generation of related blog entries in a graph form is not a bad idea,
as the resulting graphs look promising. You can see them [here](/website-map).


>Albums: <br>
>Dawid Podsiadło - Leśna Muzyka<br>
>Cory Wong - Wong's Cafe<br>
>Books:<br>
>Busy Doing Nothing - 100 Rabbits<br>
>Imperium Chmur - Jacek Dukaj<br>
>The Hitchhiker's Guide to the Galaxy - Douglas Adams<br>

```
17.07 
```

Reading & thinking about graphs visualisation, both for the website and for my masters thesis. There seems to be plenty of papers exploring the matter, but not a lot of software which will let me experiment straight away (`graphviz` and `networkx` is all I found so far).

I like the idea of using physical modeling of objects such as springs to create graph layouts. This approach allows the structure to grow dynamically in real time, which makes interactive visualisations possible.

As for my masters, I'm devoting too much time thinking about the visualisation side. The core idea is to automatically create a DSP pipeline that would mimic a sample, given by the user. I'm planning to use a genetic algorithm to optimize the pipeline graph. This is similar to the popular YouTube videos where randomly generated creatures are trying to walk. I'm gonna be creating organisms which dwell in the realm of sounds :) I really want to visualise the evolution process of theese creatures and watch how their DSP-node-based bodies evolve to create various timbres, with animations and a possibility to interact with the process. I hope that explains why I'm kind of obsessed over the visualisation part.

>Albums:<br>
>Boy Harsher - Careful
