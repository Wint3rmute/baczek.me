---
title: 2025's Devlog
tags: journal, programming, culture
---

<!---->
<!-- Placeholder for my end of 2025 notes: -->
<!---->
<!-- I have never been more active in a year. Paste some Garmin stats regarding -->
<!-- running/gym My career into a leading/managing role is progressing quite -->
<!-- smoothly. I can delegate effectively, a skill I find the most important. -->
<!---->
<!-- Secondly, compared to the previous year, I think I have more patience and -->
<!-- kindness towards people around me, as communication is becoming more and more -->
<!-- important. -->
<!---->
<!-- I moved away from figuring out how implement a piece of code and make multiple -->
<!-- pieces work together. I now figure out how to teach a team member how to -->
<!-- operate within some domain space and how to effectively arrange diverse -->
<!-- interests of my coworkers together, giving them space to learn and achieve -->
<!-- great things! -->
<!---->

```
1X.07
```

{{image (src="/squash_stroke.jpg" small=true title="Squash Stroke by Harold Edgerton.")}}

I will use this image when writing about data visualisation.

---

Run my first 10k in under 1h.

> Watching:
>
> - A Bronx Tale (1993)
> - Escaflowne (2000)

```
0X.07
```

Continuing with my vibe-coding detour with [ReqSnake](/reqsnake). Migrated away
from Cursor free tier to Claude Code and I am blown away with the experience.
The comparison is no way fair, as I moved from free-tier Cursor to paid-tier
Claude, but I am still blown away. Claud suggests multiple useful patterns and
implements them quite effortlessly. It taught me about a feature of Python I did
not know - [Protocols](https://typing.python.org/en/latest/spec/protocol.html).

By the way, I'm absolutely loving [ruff](https://docs.astral.sh/ruff/) right
now. While working with Claude, I've been tweaking its configuration while the
AI was coding. The feature set of Ruff is out of this world, autofixes work
flawlessly and it all runs **so darn fast**. Best tool I've seen when it comes
to force LLMs to write quality code without a ton of prompts.

> Listening:
>
> - Together - Pejzaż Remix
> - Thievery Corporation - Temple of I&I
>
> Watching:
>
> - Tokyo Gore Police (2008)

```
3X.06
```

Confused by [Thermodynamic Computing](https://knowm.org/thermodynamic-computing/).

Discovered [Carceri d'invenzione](https://en.m.wikipedia.org/wiki/Carceri_d%27invenzione),
strangely similar to my beloved [Blame](https://en.wikipedia.org/wiki/Blame!),
but 300 years younger.

> Listening:
>
> - Genesis Owusu - No Looking Back
>
> Watching:
>
> - Prospect (2018)
> - Nausicaä of the Valley of the Wind (1984)

```
2X.06
```

Vibe-coding (there, I said it!) a small application for [requirements
management](https://en.wikipedia.org/wiki/Requirements_management) within
Markdown files. Sounds like the right project scope for the current maturity of
coding agents. The UX of [Cursor](https://www.cursor.com/) has been really nice
so far!

5 days later, there we are! [ReqSnake](https://github.com/wint3rmute/reqsnake).
My notes and observations are noted [here](/reqsnake).

---

Attempting to understand how Blindsight was shaped by [the thoughts of Thomas
Metzinger](https://youtu.be/mthDxnFXs9k?si=cgENR_MUPJH-1QZY).

> Listening:
>
> - Hiatus Kaiyote - Chivalry Is Not Dead
>
> Watching:
>
> - [Richard Penrose - Why Intelligence Is Not a Computational Process](https://youtu.be/iTVN6tFknCg?si=f_8wIdZ4dRsz_qpi)

```
1X.06
```

Organizing my software design & specification knowledge as my team size is
growing. I currently manage 8 people directly and around 3 indirectly. My
semi-formal style with clearly described tickets but no well-formalized
overarching vision is no longer scaling. I'm talking something more than
[ARCHITECTURE.md](https://matklad.github.io//2021/02/06/ARCHITECTURE.md.html)
and a set of design notes on an internal wiki.

Learning about enterprise-scale requirements management software, such as [IBM
Doors](https://en.wikipedia.org/wiki/DOORS) and [Enterprise
Architect](<https://en.wikipedia.org/wiki/Enterprise_Architect_(software)>).
They cause **so much** mental overhead and seem to be tailored for a
_blue-collar_ _Windows-only_
_I-will-not-stand-anything-that-is-not-reminiscent-of-msoffice_ mindset. I
wonder if anything like this, but much more minimal, can be created for
developers. Can't we just have a set of tags for Markdown/RST documents? With a
[lockfile](https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html)
to detect changes/inconsistencies (such as accidentally removing requirements)
and VCS integration to track status changes in Git?

> Reading:
>
> - [IEEE Standard for Information Technology - Software Design Descriptions](https://standards.ieee.org/ieee/1016/4502/)

```
0X.06
```

While playing around with 2 really nicely designed Rust frameworks,
[Dioxus](https://dioxuslabs.com/) and [Bevy](https://bevyengine.org/), I
realized that my trusty old ThinkPad x260 is having trouble keeping up with my
development workflow. A peek at [btop](https://github.com/aristocratos/btop)
reveals that:

- `rust-analyzer` is using around 4GB of RAM
- `rustc` is peaking around 1GB
- Firefox tabs are taking around 2GB
  - ... and don't even think about launching Spotify! Btw: unexpected gem - [ncspot](https://github.com/hrkfdn/ncspot)
- Add OS usage to the mix and you will soon run out of RAM!

Being too lazy to write a long post about how mad I am about increasing
resource requirements, I bought a 16GB RAM module and replaced my current 8GB
module. RAM issues gone. Thank you, ThinkPad!

> Listening:
>
> - Sroka - La Nuée

```
3X.05
```

Finished my second reading of Blindsight, a book unbelievably densely packed
with philosophophical and technological concepts, hidden in a labirynth of
techincal jargon. My favorites:

- Form Constant (Klüver constant)
- Being No One (Thomas Metzinger)

.. of course, the core plot twist is also on my list , but I'm not gonna reveal
it here!

New quotes are lading in [the quotes room](/thinking).

After reading online reviews, possible similar materials:

- Remaining books by Peter Watts, obviously
  - [Also a talk of his](https://youtu.be/v4uwaw_5Q3I?si=mikXz-B8uJJfKAEN)
- Greg Egan
  - Diaspora
  - Permutation City

```
2X.05
```

Trying to get more comfortable with CAD software. Every now and then, during a
lazy Sunday afternoon, I dedicate 2-3 hours to measure and model a random object
at my house. CAD-based modeling is far more intuitive to me than Blender-like
workflows. Perhaps my mind is deeply shaped with programming-based approaches
to things and I find parametric modeling to be a reflection of declarative
programming. Well, whatever works.

{{image (src="/focal_onshape.jpg" small=true title="Model of a Focal speaker at my family's house.")}}

> Watching:
>
> - Orphan Black, season 4
>
> Listening:
>
> - Nujabes - Luv (sic) pt2 (damn, the saxophones are so good here)

```
1X.05
```

Enjoyed [It Awaits Your Experiments by Peter Watts](https://www.rifters.com/crawl/?p=11511).

> Watching:
>
> - Orphan Black, season 4
>
> Reading:
>
> - Peter Watts - Blindsight (this time the original version, in English)

```
XX.04
```

Focused on work and healthy lifestyle for the entire month, had no time to note
anything here.

Run my first 10k.

> Watching:
>
> - Orphan Black, seasons 1-3

```
1X.03
```

Thinking about data sonification again. [The Digital
Heartbeats](https://youtu.be/J81WQrIBrpw?si=nBZ0eAcowzNqSEZM) sparkled some new
ideas in my mind. Using code coverage data ([Python's
trace](https://docs.python.org/3/library/trace.html), [Clang's
SanitizerCoverage](https://clang.llvm.org/docs/SanitizerCoverage.html)) as it
runs in real time could be used to draw visualisations or play sonifications
describing what's going on. I'm pondering on an idea of the _shape_ of a
running program and how it could evolve with different usage patterns of the
same application. If the visualisation/sonification tool is written correctly,
the _shape_ could be preserved between application versions, altering only
slightly.

> Watching:
>
> - A Rainy Day in New York (2019)
> - Severance, season 2
>
> Reading:
>
> - Blame! (1997, second time)

```
0X.03
```

> Watching:
>
> - Coherence (2013)
> - The Substance (2024)
>
> Listening:
>
> - Vulfpeck - New Beastly
> - Magdalena Bay - Mercurial World

```
2X.02
```

{{image (src="/iceland_2025.jpg" small=true title="Visiting Iceland.")}}

> Reading:
>
> - Don Norman - The Design Of Everyday Things
>
> Listening:
>
> - Son Lux - Risks of Make Believe

```
1X.02
```

> Reading:
>
> - Greg Egan - Learning To Be Me
> - [C2 Wiki - Anti Patterns Catalog](https://wiki.c2.com/?AntiPatternsCatalog)
>   - Also available on [antipatterns.com](http://antipatterns.com/briefing/sld001.htm)
>
> Watching:
>
> - The Brutalist (2024)

```
0X.02
```

> Listening:
>
> - Twenty One Pilots - Clancy
> - Robert Sapolsky - Human Behavioral Biology
>
> Watching:
>
> - The Banker (2020)
>
> Reading:
>
> - Pat Helland - Immutability Changes Everything

```
2X.01
```

Took a small movie-making (or rather video-tutorial-making) task at work, to
get a break from programming/managing/whatever it is that im currently doing.
Happy to report that DaVinci Resolve works like a charm on Linux, with full
GPU support! Together with Bitwig, i can basically do whatever I want, without
leaving the comfort of my Arch setup.

> Playing:
>
> - Ultrakill
>
> Listening:
>
> - Heaven Pierce Her
>
> Reading:
>
> - [Testing Angular](https://testing-angular.com/)
> - [Lars Wirzenius - 40 years of programming](https://liw.fi/40/)

```
1X.01
```

> Watching:
>
> - Porco Rosso (1992)
> - Dune: Prophecy (2024)
> - El Topo (1970)

```
0X.01
```

Using last free days after christmas/new year to do some work on my infrastructure:

- All of my [hosted services](/decentralisation) are now rate-limited. Sorry, bots!
  - Rate limiting is not very agressive, but [contact me](/contact) if you encounter issues
- Everything is now [HTTP/3](https://en.wikipedia.org/wiki/HTTP/3) compliant
- I've set up [Borg backup](https://github.com/borgbackup/borg) for private stuff on my homelab. It's now using a multi-level backup strategy:
  - RAID1 on ZFS
  - ZFS snapshots (working on it)
  - ZFS snapshots with `sanoid`
  - Backup to a remote location via Borg
- I have migrated away from Google Photos and Google Drive, everything is now
  kept on my private cloud

> Watching:
>
> - The Florida Project (2017)
> - Jacob Collier - [Logic Session Breakdown: Little Blue](https://youtu.be/M-Ii2_GgdRs?si=Mik_xJahM9wZ0Sup)
>
> Listening:
>
> - PJ Morton feat. Yebba - How Deep Is Your Love

---

<br>

Go back to [2024](/2024).

<br>
