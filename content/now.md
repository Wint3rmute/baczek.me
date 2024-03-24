---
title: 2024's Devlog
tags: journal, programming, culture
---

<!-- S05E14 -->

```
2X.03
```

>Watching:
>
>- Dune: Part Two
>- The Holy Mountain (1973)
>
>
>Reading:
>
>- [NixOS in Production](https://github.com/Gabriella439/nixos-in-production)
>- Cixin Liu - Theee Body Problem
>
>Listening:
>
>- Lor

{{image (src="/lor.jpg" small=true title="The band Lor in Niebo, Warsaw")}}


```
1X.03
```

Finally having some time to play around with the
used Octatrack unit I bought a couple months ago. It
still surprises me how much hardware-centered music
making machines feel similar to terminal-based tools
such as bash/zsh/nu and vim.

Still fiddling with [NixOs](/nixos), making tiny steps towards
using it as a daily driver.

```
0X.03
```

>Watching:
>
>- Crumb (1994)
>
>Listening:
>
>- Ryuichi Sakamoto - Merry Christmas Mr. Lawrence
>- Jacob Collier - Djesse Vol. 4

A pleasant surprise: *Djesse Vol. 4 - Box Full Of Stars Pt. 2* contains a few
words in Polish at `2.15`


```
2X.02
```

Picked up an Arduino and started playing around with
Rust for AVRs.

>Watching:
>
>- Hayao Miyazaki - The Boy and the Heron
>- David Lynch - Dune
>
>Listening:
>
>- Son Lux - Prophecy
>- Daft Punk - Infinity Repeating


```
1X.02
```

TODO: add note on making myself look like an idiot when attempting to contribute to nixpkgs.

>Listening:
>
>- Daft Punk - Human After All
>- Alan Parsons Project - Ammonia Avenue


```
0X.02
```

>Listening:
>
>- Robert Sapolsky - Human Behavioral Biology
>
>Reading:
>
>- Peter Watts - Behemoth


```
2X.01
```

Done some optimisations of my infrastructure:

- All services are now accessible from IPv6
- Switched from TCP to UNIX sockets in the Postgres database used
  by [Invidious instance](https://invidious.baczek.me/)
- Fine-tuned Postgres with
  [PGTune](https://pgtune.leopard.in.ua/), hoping to see some
  results in my monitoring. Doing that configuration via
  [NixOs](/nixos) was a breeze

To my surprise, after 2 days I took a look at my monitoring
charts and saw visible improvements in my metrics:

- CPU usage is down **a lot**
- Almost 3 times less IO operations are performed
- CPU temperature is down **by 10℃**

..all of that while the request rate reported by Caddy hasn't
changed!

{{image (src="/metrics_pgtune.png" small=true title="Metrics from [Node Exporter](https://github.com/prometheus/node_exporter). Light-blue line marks the moment when PostgreSQL tunings were applied.")}}

---

Went back to my [Invidious MR adding Prometheus
metrics](https://github.com/iv-org/invidious/pull/3576).

>Listening:
>
>- Depeche Mode - Exciter
>
>Watching:
>
>- Ennio (2021)


```
1X.01
```

Broke my whole IT infrastructure for 12+ hours due to a trivial mistake in
static IP configuration. I haven't noticed it until late afternoon, the fix was
rather easy but I learned a bit about `nmcli`. Funny adventure, worth it :)

Week 1 of going to the gym!

Bought a used Octatrack unit. I already have to hold myself back from tinkering
with it instead of during house chores. Once I connect my piano to it I'm gonna
be out for at least a few days :) The workflow is wonderful and the idea of
having a single "macro knob" is both simple and effective.

>Reading:
>
>- Peter Watts - Maelstrom
>
>Listening:
>
>- Vulfpeck - Live at Madison Square Garden
>- David Bowie - Sound and Vision (the pure piano version)


```
0X.01
```

Finished migrating my cloud & home instrastructure to [NixOs](/nixos). It
really feels like an improvement over Ansible playbooks (although I am still
using them for copying files & running system rebuilds, it is the easiest
solution for me), as I can merge custom software builds/packaging with the system
setup & configuration. Learned a bit about [`nftables`](https://nftables.org)
in the process.

Trying out some funky rhytms - learning how to play Beastly by Vulfpeck. Amazed
to see that they've made [an official
tutorial](https://www.youtube.com/watch?v=KQRV0c1KXYc) on that song and some
others.


>Reading:
>
>- Peter Watts - Starfish
>
>Listening:
>
>- Nicolas Jaar - Space Is Only Noise If You Can See
>- Jungle - For Ever
>- Kenny G - Sade
>- Lovage et al. - Music to Make Love to Your Old Lady by

---

<br>

Go back to [2023](/2023).

<br>
