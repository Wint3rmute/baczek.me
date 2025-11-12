---
title: Sonification
---

Notes on [data sonification](https://en.wikipedia.org/wiki/Sonification).
In my daily job, I am often watching over multiple streams of logs and metrics.
Processing all this information just by eyes sounds like a waste of resources.
We've built data visualisation tools so that we can utilize our visual cortex
for "free" data pre-processing. Why not use other senses?

Thinking about a rich data sonification system. Brain dump:

- For raw textual logs, flow rate as a sub-bass signal. More logs, higher
  frequency or a filter opening up
- Alternative for the bass, an ambient sample, something from Brian Eno's
  *Music for Installations*, rising in volume with the logs flow rate
- A log filtering engine, as simple as mapping "`regex → sound`". All matches are
  fed into a sound generator as MIDI-like events, with some debouncing applied
- Automatic determination of a "nominal" flow rate of all logs or just filtered events.
  Second-order derivative and some inertia? Or maybe just a simple moving average?
