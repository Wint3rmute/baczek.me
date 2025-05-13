---
title: 2025's Devlog
tags: journal, programming, culture
---

```
1X.05
```

Enjoyed [It Awaits Your Experiments by Peter Watts](https://www.rifters.com/crawl/?p=11511).

> Watching:
>
> - Orphan Black, season 4

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
