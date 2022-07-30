---
title: 2022's Devlog
---

```
DD.MM
```

Devlog format, first try.

Description of things I'm working on

>Culture I've read/heard/experienced in other ways

*TODOs and other comments*

```
29.07
```

Exploring ideas related with sound fingerprinting and song similarity calculation. *Computer Vision for Music Identification* is the most interesting paper I've found so far. Even in such niche use cases, [Arch Linux repos still deliver](https://archlinux.org/packages/extra/x86_64/chromaprint/). 

{{image (src="/olsztyn-festival-logo.jpg" title="Logo of a music/art festival in Olsztyn. Ulotny is a play on words, meaning both something passing, transitory, delicate and something that can fly away, hence the airship :)") }}

```
26.07 
```

Busy sailing with friends at Mazury, a region of Poland with lots of nice lakes. Sailing helps a lot when taking a break from technology as I don't get bored watching the waves, boat and landscapes around. 

I finally have some time to dig through The Rust Book now :)

![Sailing. Mazury, Poland](/sailing_mazury.jpg)

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
