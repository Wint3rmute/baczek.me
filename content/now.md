---
title: 2022's Devlog
---

```
15.11
```

Ported `mverb` to Rust! I'm still fixing some bugs, but it's usable overall. The code is currently embedded inside [Libretakt](https://github.com/Wint3rmute/Libretakt), but I'm planning to release it as a standalone crate when I'm done with this semester.

---

Watched a talk on [neural audio effects](https://github.com/csteinmetz1/NeuralReverberator). The project is insanely cool and the author's github is a goldmine of interesting audio programming resources. 


```
12.11
```

Finally learning about digital filters, as I don't want to rely only on off-the-shelf filter implementations while working on [Libretakt](https://github.com/Wint3rmute/Libretakt). 

[Youngmoo Kim's](https://m.youtube.com/channel/UC4Emb8dzcIBEMQG2UfDoD8w) DSP videos are a great learning resource if you're starting from scratch and want to learn some theory. 

---

TIL: Urs Heckmann, creator of the [Diva Synth](https://u-he.com/products/diva/) (Ben Bohmer's main VST of choice) runs a [blog](https://urs.silvrback.com/)! 

---

Deployed [watchtower](https://github.com/containrrr/watchtower) on my server to automatically update the [public services](https://baczek.me/decentralisation/) I'm hosting.

>Listening:<br>
>Dawid Podsiadło - Szarość i Róż<br>
>Ghost in the Shell OST - Floating Museum


```
08.11
```

Since the start of this semester, I'm feeling like my country's education system is constantly overwhelming the students with the amount of things to learn and projects to finish. Similar thoughts have been circulating in my head long before, but I feel like I need to vent them out. 

Due to the information/work overload, students no longer actually *learn* anything on a deeper level, they just skim over the bare minimum required to finish a project. There's just no other way to keep up with all work.

Somewhere in the process of improving the education system, we fell victim to the [Goodheart's Law](https://en.m.wikipedia.org/wiki/Goodhart%27s_law). Blindly increasing the amount of information  learned by students just for the sake of ECTS or some other university-related metric does not actually increase the amount of knowledge that the students are gaining. 

{{image (src="/computer_poster.jpg" title="How it should feel like to use the Internet")}}

*Todo*: trim the right side of this poster. 

>Listening:<br>
>Cory Wong & Dirty Loops - Follow The Light<br>
>Dawid Podsiadło - Project 19<br>
>Oliver Koletzki - I am OK

```
27.10
```

Found out about [Hania Rani](https://haniarani.com/) today. Glad to see more talented Polish artists doing experimental music :) 

>Listening:<br>
>Hania Rani - Eden<br>
>Thievery Corporation - Love Has No Heart


```
22.10
```

Found out about [dragon](https://github.com/mwh/dragon)
while searching for possible improvements to my terminal workflow.

*TODO*: a summary of my favourite terminal utilities, especially
the less popular ones.


```
18.10
```

Slimming down the docker image I'm using to generate the related posts [map](/map).

Again, thinking about rewriting the whole thing completely from scratch, just to learn some low level NLP, as the image is still way over 1GB.

```
17.10
```
Finished watching [this brilliant talk](https://www.youtube.com/watch?v=vn7563IAQ_E) by [timur.audio](https://timur.audio/). A true eye opener, as I was mostly ignorant of C++ standard's inner workings regarding real-time guarantees. 

Rewriting [Libretakt's](https://github.com/Wint3rmute/Libretakt) cross-thread data synchronisation mechanism to [mpsc](https://doc.rust-lang.org/std/sync/mpsc/) (or some other lock-free communication primitive, only time will tell).

---

Update: settled down on [Flume](https://github.com/zesterer/flume) for
lock-free communication.

>Listening:<br>
>The Chemical Brothers - No Geography<br>
>The Killers - When You Were Young<br>
>Panic! At the Disco - New Perspective

```
10.10
```

I should write a post on cosmic horror movies/books/etc


```
08.10
```

I often find myself mistaking the command which launches [Orca screen reader](https://help.gnome.org/users/orca/stable/)
with the one launching the [Orca sequencer](https://github.com/hundredrabbits/Orca) (commands are `orca` and `orca-c` on my system, so it's easy to get them wrong).
This gave me an opportunity to dig a little bit into the screen readers world.

I was really impressed that every single UI element of Firefox is compatible with `orca`. This adds a completely new layer to UI programming,
I really feel ignorant for not realising this before.

I've heard that the only way to actually make your websites accessible for people with vision disabilities is to use them
the same way they do, so I gave my website a try while blinded, using some basic keyboard shortcuts i found via `man orca`.
I was able to get around the page without any issues, so I guess that's another reason to stay minimal with your site. Also, using proper semantic tags (nav, section, etc) is always a good idea!


TODO: On the other hand, thinking about my interest in data visualisation

```
07.10
```

Updated the related pages generation system for Python 3.10 compatibility. The amount of dependencies required
to run the generation script is staggering. 292 Fedora dependencies and 111 Python libraries!

Idea: try writing a basic word vectorizer and a PCA algorithm, see how it performs as a minimal setup.

---

Going down the real-time video/audio streaming rabbit hole again, this time for
a university project - real-time sound synthesis and streaming to an arbitrary
number of connected devices, all collaborating together to create a track. Synthesizer as a service?

>Listening:<br>
>Punch Brothers - Familiarity<br>
>Apollo - Brian Eno


```
01.10
```

Clearing code and fixing the AUR package of my old project, [Telegram Notification Bot](https://github.com/Wint3rmute/tnb). Reading on de-bloating and improving build times of Rust programs.

>Listening:<br>
>Ben Bohmer - Lost in Mind

```
25.08
```

Experimenting with wavetable synthesis. I've managed to hack it into [nosna](https://github.com/Wint3rmute/nosna) and sampled my Minilogue, just to have some "homemade" wavetables. It's way more entertaining than coding an FM synthesiser, as you can get a lot of interesting timbres without having to play around with operator ratios & envelopes. This "happy accidents" workflow is more enjoyable and rewarding. On the other hand, it mostly boils down to the samples you're using to build the wavetables. 

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

Dredd was surprisingly fun to watch, if you enjoy cliche sci-fi movies or action movies in general, you're going to have a good time.

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

It's amazing how the voices of the audience synchronise together at the end when the music stops, it was almost a spiritual moment for me while listening.

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
>Beardyman & MC Hyperscott: Shelter me from the rain


```
04.08
```

Added stemming to the algorithm generating related posts, I'm seeing a lot of improvement!

{{image (src="/xxiivv_umap_stemming.jpg" title="After stemming, clusters are clearly visible, even when fully unzoomed.
I am still testing on XXIIVV blog contents, as it has lots and lots of posts.") }}


```
03.08
```

Experimenting with [UMAP](https://umap-learn.readthedocs.io/en/latest/) for [related posts exploration](/map).
I'm testing it on [XXIIVV](http://xxiivv.com/) again, but this time **without cheating**, preprocessing removes
the `<nav>` blocks containing links to other pages, the algorithm works only with each page's content. Results are promising:

{{image (src="/xxiivv_umap.jpg" title="Portion of the projection generated by UMAP.") }}

>Music:<br>
>Al Steward - Year of the Cat


```
01.08
```

Cleaned up the site deployment code, moved the docker image to Fedora + Python3.9 (3.10 does not yet have wheels for `sklearn` and there are some problems with numpy compatibility). I'm now ready to test UMAP for [site map](/map) generation :)

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
as the resulting graphs look promising. You can see them [here](/map).


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
