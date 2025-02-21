---
title: 2025's Devlog
tags: journal, programming, culture
---

```
2X.02
```

> Reading:
>
> - Don Norman - The Design Of Everyday Things

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
