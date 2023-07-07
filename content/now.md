---
title: 2023's Devlog
tags: journal, programming, culture
---

```
07.07
```

>Listening:
>
>- a-ha - Summer Moved On


```
02.07
```

>Watching:
>
>- Lost (Season 4)
>
>Reading:
>
>- Peter Watts - Echopraxia
<!-- S04E07 -->


```
28.06
```

Grabbing some air after the last master's semester. I'm glad to notice that my
mind has again started to produce ideas for extending my projects. Starting to
rewrite [Libretakt's](https://github.com/Wint3rmute/libretakt) user interface
to work as a website-based remote controller to the sampler engine. Networking
code is going to get simpler as the a single sampler instance is meant to be
run only locally. [Egui](https://egui.rs) should work just fine for a mobile-first
user interface.

>Watching:
>
>- Asteroid City (2023)
>
>Listening:
>
>- Boy Harsher - The Runner


```
22.06
```

>Watching:
>
>- Lost (Season 3)


```
18.06
```

~~Created [AreWeSpaceYet.com](https://arewespaceyet.com) as a 1-day project.~~
**Edit (29.06):** removed AreWeSpaceYet.com since its a duplicate of the
[AeroRust](https://aerorust.org/) website, which already has lots of
interesting content on using Rust in aerospace.

>Watching:
>
>- Lost (Season 2)


```
15.06
```

>Reading:
>
>- [Effective Rust](https://www.lurklurk.org/effective-rust/)
>
>Watching:
>
>- Lost (Season 1)


```
12.06
```

Converted my [website map](/map) generation algorithm from using TFIDF to [text
embeddings](https://www.sbert.net/), I'm seeing a lot of improvement in how the
generated map looks! It's a pretty lightweight solution (if you're not counting
the `torch` library which is a behemoth), the embeddings only weight ~90MB.
The embeddings really capture the general context between posts that they put
closely together.


```
11.06
```

Finishing touches on my [master's thesis](/luthier).

Started hosting [Libreddit](https://libreddit.baczek.me).

Fell in love with [unplug.red/automatism](https://unplug.red/automatism/),
haven's seen such a beautiful website in a long time.

>Listening:
>
>- Oneohtrix Point Never - The Pure and the Damned
>- Junior - Bluszcz


```
06.06
```

>Watching:
>
>- The Endless (2017)
>
>Listening:
>
>- Brodka - Wpław - Skalper Rework
>- Rob Doughan - Clubbed to Death
>- Joris Delacroix - Homie
>- Moby - Long Ambients 1: Calm. Sleep


```
03.06
```

{{image (src="/vl1_manual.jpg" small=true title="Old synth manuals aesthetics")}}

>Listening:
>
>- Baasch - Wosk


```
30.05
```

>Watching:
>
>- Videodrome (1983)
>- The Fly (1986)


```
28.05
```

>Watching:
>- The Green Knight (2021)
>
>Listening:
>- BØRNS - Past Lives


```
24.05
```

In the middle of writing my master's thesis.

>Watching:
>- Beau is afraid (2023)
>- Watchmen (2009)


```
18.05
```

>Reading:
>- David B. Lamkins - [Successful Lisp](https://dept-info.labri.fr/~strandh/Teaching/MTP/Common/David-Lamkins/cover.html)
>
>Listening:
>- Kraftwerk - Computer World
>- Yumi Zouna - In Camera

```
13.05
```

{{image (src="/luthier_simple_analog.png" title="Evolving parameters of simple DSP graphs")}}

>Listening:
>- Nation of Language - Introduction, Presence

```
06.05
```

>Listening:
>- Yumi Zouma - In Camera


```
02.05
```

Switched all my computers to [Arch Linux](https://archlinux.org/), automated the
process of deploying my [system
configuration](/linux). Spent some time merging
my configuration repositories and documenting the result.

Exploring ideas related with genetic programming, mainly how one should
represent the structure of an optimisation problem in a form that would be
viable for genetic programming approach. [Mixed type cartesian genetic
programming](https://www.researchgate.net/publication/224041240_MT-CGP_Mixed_type_cartesian_genetic_programming)
was the most interesting approach so far.

>Watching:
>- Alan Kay - [The computer revolution hasn't happened
>  yet](https://www.youtube.com/watch?v=oKg1hTOQXoY)
>
>Listening:
>- Son Lux - *Ghost Melody*

---

Started collecting some [thoughts on thinking](/how-to-think).

{{image (src="/blue_thoughts.jpg" small=true title="You have to have something blue, to have blue thoughts with.")}}

```
29.04
```

Switched to [Nu Shell](http://www.nushell.sh/), learning about new ideas for OS
shells which Nu is exploring.

Automating the deployment of my system configuration with
[Ansible](https://github.com/Wint3rmute/dotfiles/blob/master/playbook.yml).

---

[Gerald Sussman](https://en.wikipedia.org/wiki/Gerald_Jay_Sussman) on [why MIT
has switched from Lisp to
Python](http://wingolog.org/archives/2009/03/24/international-lisp-conference-day-two)
in their introductory programming courses:

>Engineering in 1980 was not what it was in the mid-90s or in 2000. In 1980,
>good programmers spent a lot of time thinking, and then produced spare code
>that they thought should work. Code ran close to the metal, even Scheme -- it
>was understandable all the way down. Like a resistor, where you could read the
>bands and know the power rating and the tolerance and the resistance and V=IR
>and that's all there was to know. 6.001 had been conceived to teach engineers
>how to take small parts that they understood entirely and use simple
>techniques to compose them into larger things that do what you want.
>
>But programming now isn't so much like that, said Sussman. Nowadays you muck
>around with incomprehensible or nonexistent man pages for software you don't
>know who wrote. You have to do basic science on your libraries to see how they
>work, trying out different inputs and seeing how the code reacts. This is a
>fundamentally different job, and it needed a different course.


```
21.04
```

Full focus on master's thesis!

>Reading:
>- Terry Pratchett - Moving Pictures
>
>Listening:
>- user18081971 - qu 1
>- Aphex Twin - Alberto Balsalm
>- Vulfpeck - I Can't Party


```
17.04
```

>Watching:
>- Wes Anderson - Moonrise Kingdom
>- Wes Anderson - The Royal Tenenbaums
>- Wes Anderson - Bottle Rocket
>
>Listening:
>- Joe Hisaishi - Merry-Go-Round of Life


```
12.04
```

>Watching:
>- Werner Herzog - On Death Row
>
>Listening:
>- Yazoo - And On
>- Todd Terje, Bryan Ferry - Johnny and Mary


```
07.04
```

Had a breakthrough moment with Lisp, finally
understanding the idea behind "code is data".
Rethinking my approach to type systems and
programming language architecture. All things
Lisp-related are food for thought :)

>Watching:
>- [MIT 6.001 - Structure and Interpretation](https://www.youtube.com/playlist?list=PLE18841CABEA24090)
>
>Reading:
>- Peter Watts - Blindsight


```
03.04
```

Played a first jam session in my life :)

>Listening:
>- The Doors - Riders on the Storm


```
31.03
```

Trying to wrap my head around the database-centered
(Postgres-centered in my case) approach to building web
applications, especially:

- Declarative APIs, taken from the DB model (think [Hasura](https://hasura.io/))
- Storing business logic in the DB instead of relying on application-level validation

Learning how to minimize writing glue code and focusing on delivering value.

>Listening:
>- KARAŚ/ROGUCKI - Czułe Kontyngenty


```
28.03
```

>Reading:
>- Terry Pratchett - Mort
>
>Listening:
>- RY X - Bound (Live from the Royal Albert Hall)
>- KARAŚ/ROGUCKI - Jutro Spróbujemy Jeszcze Raz
>- sanah - wars
>
>Watching:
>- Avatar - The Way of Water


```
20.03
```

>Reading:
>- Terry Pratchett - Eric


```
13.03
```

Re-learning `egui`, works wonderfully for making interactive
node graphs!

>Reading:
>- Terry Pratchett - Sourcery
>
>Watching:
>- David Lynch - Blue Velvet
>
>Listening:
>- Roy Orbison - In Dreams
>- Jack Stauber - Cheeseburger Family


```
05.03
```

Moving website generation to GitHub actions. Considering
migrating my VPS to ansible-managed.


```
02.03
```

>Reading:
>- Terry Pratchett - Making Money
>
>Listening:
>- Nation of Language - On Division St
>- Ásgeir - Snowblind


```
22.02
```

Starting to think about the visual representation of the
graph I'm gonna be evolving for my [master's
thesis](/luthier)


```
18.02
```

Learning Ansible, taking care of servers at work.

>Listening:
>- Depeche Mode - Ghosts Again
>- Cautious Clay - Cheesin'
>- Jacob Collier - Hajanga
>- Juno Reactor - Guardian Angel


```
04.02
```

Reliving the cartoons from my childhood. Amazed to see that their
[website](https://en.codelyoko.fr) is still alive and active!

>Watching:
>- Code Lyoko
>
>Listening:
>- Aphex Twin - Selected Ambient Works
>- Passenger - Things That Stop You Dreaming
>- Kishi Bashi - 151a
>- Sleeping At Last - You're Enough
>- Depeche Mode - The Love Thieves
>- Brian Eno - LUX 1


```
28.01
```

Recorded a small
[demo](https://odysee.com/@Wint3rmute:c/libretakt_demo:2) of
[libretakt](https://github.com/Wint3rmute/libretakt/) - a sampler
I've worked on during a university course.

>Reading:
>- H.P. Lovecraft - At the Mountains of Madness
>
>Watching:
>- Ghost in the Shell 2: Innocence


```
27.01
```

Exploring ideas related with [decentralised](/decentralisation)
search engines. Wrote a small manifesto on a
[new paradigm for how we search the web](/search-registry-manifesto).

>Watching:
>- The Call Of Cthulhu (2005)
>
>Listening:
>- Aphex Twin - #3
>- Cory Wong - Power Station Tour


```
21.01
```

Starting to work on [generating synth pathes](/luthier) from audio samples!

>Listening:
>- Rysy - Traveler
>- Son Lux - Plans We Made
>- Fiora - Let It Go By
>- LCD Soundsystem - Home
>- MC Virgins - Sundress
>(guilty pleasure, obviosly. Helps getting through the semester though)


```
17.01
```

Did a minor contribution to [Mutable Instruments' documentation
repo](https://github.com/pichenettes/mutable-instruments-documentation). Glad
to see that I'm getting more comfortable with suggesting patches to various
open-source projects! Also glad that it's possible to "just submit" a
suggestion to software written by a prominent artist. Despite all the
negativity coming from the media and politics, we live in a great age :)

>Listening:
>- Boa - Duvet
>- Vulfmon - Boogie Man
>- Jeanette - El Muchacho de los Ojos Tristes
>- Rysy - Wyspa
>- Rysy - Przyjmij Brak


```
14.01
```

>Listening:
>- Carbon Based Lifeforms - Live at Ozora Festival 2017


```
10.01
```

{{image (src="/virgin_fail.jpg" title="Sad news from Virgin Orbit")}}

Not a good day. Those cubesats really had potential :(


```
09.01
```

{{image (src="/website_footprint.jpg" title="Getting there!")}}

>Watching:
>- Guillermo del Toro's Cabinet of Curiosities
>
>Listening:
>- Vulfpeck - Schvitz
>- T.Rex - Get It On (Virgin Magnetic Material remix)
>- Virgin Magnetic Material - LBDs mixtape

```
05.01
```

>Reading:
>- Sean Luke - Computational Music Synthesis
>
>Watching:
>- Warner Herzog - The Enigma of Kaspar Hauser


```
02.01
```

Mood: reverb diagrams aesthetic.

{{image (src="/simple_reverb_loop.jpg" small=true noshadow=true title="Simple
reverb loop. Taken from <a
href='http://www.spinsemi.com/knowledge_base/effects.html'>spinsemi.com</a>")}}



```
01.01
```

1. Trying to improve the [website map](/map) using Graphviz's
   [gvmap](https://graphviz.org/docs/cli/gvmap/). The clusters represented
   below have no real meaning, I've added them just to see whether this idea
   makes any sense visually.

    {{image (src="/testing_gvmap.jpg" small=true noshadow=true title="Prototype of
    the website map generated with <code>gvmap</code>")}}

1. Recently edited posts are now marked with an indicator: {{image
   (src="/recent_emoji.jpg" small=true noshadow=true title="")}}

1. Added a simple tags system to post metadata, will help with map generation.

---


{{image (src="/graphviz_happy_accident.jpg" small=true noshadow=true
title="Accidentally generated this diagram by mistake. Looks pretty to me,
let's call it a happy accident!")}}


>Reading:
>- Nicholas Kristof, Shreyl WuDunn - Tightrope. Americans Reaching for Hope

---

<br>

Go back to [2022](/2022).

<br>
