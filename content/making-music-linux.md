---
title: Making music on Linux
tags: programming
---

*Trying to build a productive music-making environment as a Linux purist.*

## The Setup

- The first thing is to get JACK working on
  your system. [Arch Wiki
  page](https://wiki.archlinux.org/title/JACK_Audio_Connection_Kit)
  should have everything you need.
- [QjackCtl](https://qjackctl.sourceforge.io/)
  is a useful GUI app for managing your JACK
  configuration, it comes packaged in most
  Linux distros. Use the "graph" view to
  configure your audio devices.

## The DAW

In my opinion, the most mature DAW available for Linux is
[Bitwig](https://www.bitwig.com). It is somewhat pricey and is
not open-source, however it makes up for it with its broad range
of available synths, effects and other features. The UI feels
snappy and very intuitive. On my personal machine I feel like
Bitwig is 1.5-2x times faster than Ableton in "just doing the
general DAW stuff".

If you feel more adventurous and would like to try a more *experimental*
interface, [Bespoke](https://www.bespokesynth.com/) could be the DAW for you.

## The VSTs

- Anything from [U-he](https://u-he.com/products/) should be great if you're
  willing to pay for it
- [Dragonfly Reverb](https://github.com/michaelwillis/dragonfly-reverb) is a
  good sounding reverb, which comes in multiple variations
- Arch Linux's [pro-audio](https://archlinux.org/groups/x86_64/pro-audio/)
  package group provides a lot of up-to-date VSTs (and also other audio-related
  programs)
- *todo*: write something about [Modarrt](https://www.modartt.com/)

## The controllers

Novation's [Companion](https://us.novationmusic.com/components) software is
built around Web MIDI API, so it works on any OS which can open Google Chrome
(tested myself, unfortunately Firefox and Chromium do not work yet). This can
get you around the limitations of OS-bound apps, which are unfortunately used
by most MIDI gear manufacturers.
