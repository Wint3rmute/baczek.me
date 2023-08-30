---
title: Making music on Linux
tags: programming
---

*Trying to build a productive music-making environment as a Linux purist.*

## Initial setup, no matter what you will use later on
- The first thing is to get JACK working on your system. [Arch Wiki
  page](https://wiki.archlinux.org/title/JACK_Audio_Connection_Kit) should have
  everything you need, also for non-Arch distros.
- [QjackCtl](https://qjackctl.sourceforge.io/) is a useful GUI app for managing
  your JACK configuration, it comes packaged in most Linux distros. Use the
  "graph" view to configure your audio devices, this is incredibly useful when
  debugging audio routing which gets messy very quickly!

## The DAW

In my opinion, the most mature DAW available for Linux is
[Bitwig](https://www.bitwig.com). It is somewhat pricey and is not open-source,
however it makes up for it with its broad range of available synths, effects
and other features. The UI feels snappy and very intuitive. On my personal
machine I feel like Bitwig is 1.5-2x times faster than Ableton in "just doing
the general DAW stuff".

If you feel more adventurous and would like to try a more *experimental*
interface, [Bespoke](https://www.bespokesynth.com/) could be the DAW for you.

## The VSTs

- Anything from [U-he](https://u-he.com/products/) works on Linux and sounds
  great, but you'll have to pay for it. I especially recommend
  [Diva](https://u-he.com/products/diva/)
- [Dragonfly Reverb](https://github.com/michaelwillis/dragonfly-reverb) is a
  good sounding reverb, which comes in multiple versions, modelling
  reverberation in various spaces
- Arch Linux's [`pro-audio`](https://archlinux.org/groups/x86_64/pro-audio/)
  package group provides many VSTs (and other audio-related programs)
- [Cardinal](https://github.com/DISTRHO/Cardinal) offers a wide of range of
  Eurorack module clones, my favourite being Mutable Instruments
- *todo*: write something about [Modarrt](https://www.modartt.com/)

{{image (src="/cardinal_patch.jpg" title="Cardinal also has the cutest patch descriptions!")}}

## The controllers

Novation's [Companion](https://us.novationmusic.com/components) software is
built around Web MIDI API, so it works on any OS which can open Google Chrome
(tested myself, unfortunately Firefox and Chromium do not work yet). This can
get you around the limitations of OS-bound apps, which are unfortunately used
by most MIDI gear manufacturers.

When picking a controller, first check whether it is supported by
[DrivenByMoss](https://www.mossgrabers.de/Software/Bitwig/Bitwig.html). It will
get you an out-of-the-box full DAW integration, just like between Ableton &
Ableton Push. I cannot recommend it enough!
