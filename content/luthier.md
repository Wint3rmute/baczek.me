---
created: 2022-07-29T12:33:09+02:00
modified: 2023-04-30T12:53:05+02:00
title: Luthier
tags: culture, programming, generative
---

# Generative sound timbre design

[Luthier](https://github.com/Wint3rmute/luthier) is an experimental tool for
generating sound synthesisers, which imitate a given sound sample. I'm building
it as my master's thesis.

## Roadmap & tracking

| Week & month | Goal |
| :-- | :-- |
| w1/02 | Test FFT algos in rust, try plotting them in real time in UI |
| w2/02 | Prepare **any** prototype of synth graph building UI |
| ... | |
| Half a semester passes.. | Busy with work |
| ... | |
| w8/05 | Wrote an actual working prototype in Python          |
| w9/01 | Graph structure          |
| w9/02 | Audio playback           |
| w9/03 | Random graph generation, simple loss function  |
| w9/04 | Control signals normalisation  |
| w10/05 | Multithreading when optimising or searching through parameter space for benchmarks | 
| w10/06 | Handcoding different FM synths and trying to optimise them by stupid-simple evolutionary algorithms |
| w10/07 | Graph colorisation & animations, integration with `scipy.optimize`  |
| w11/01 | Normalised ADSR signals, reworked parameter setting. Basic one-operator FM optimised successfully! |
| w11/02 | Experiments with Frechet audio distance (abandoned, different use case than mine), rust ADSR, converting notebooks to the new rust backend |
| w11/03 | Notebook cleanup, UTs cleanup |
| w11/04 | Implemented simple virtual analog algorithms |
| w11/05 | *Cheat day* |
| w11/06 | Implemented a reverb node, successfully evolving a 2-oscillator virtual analog with reverb |
| w11/07 | basic version of generic synth genetic code |
| w12/01 | Making the presentation, evolving analog-FM hybrids  |
| w12/02 | Progress presentation seminary |
| w12/03 | A break! |
| w12/04 | Consulting my thesis advisor, MVP has been reached, time to write the thesis! |
| w12/05 |  |
| w12/06 |  |
| w12/07 |  |
| w13/01 |  |
| w13/02 |  |
| w13/03 |  |
| w13/04 | Experimenting with analog modeling, sounds quite nice now |
| w13/05 |  |
| w13/06 | Attepmting to recreate samples from Korg Minilogue, fix an insanely dumb bug with different sample rates across Python and Rust |
| w13/07 | Implementing delay, tweaking param ranges for ADSR |
| w14/01 | Testing spectrogram as target function |
| w14/02 | Testing different variations of MFCC and Fourier target functions, RMS/DTW flying all over the place |
| w14/03 | Consulted the current thesis state with the supervisor, looks good, chapter shuffling ahead |
| w14/04 | Restructured the thesis according to supervisor's directions |
| w14/05 | Equations in the problem definition chapter |
| w14/06 | Performed synthesis parameters cross-section tests of target functions |
| w14/07 | Found benchmarks of a previous thesis which I can use for comparison with my work  |
| w15/01 |  |
| w15/02 |  |
| w15/03 |  |
| w15/04 |  |
| w15/05 |  |
| w15/06 |  |
| w15/07 |  |
| w16/01 |  |
| w16/02 |  |
| w16/03 |  |
| w16/04 |  |
| w16/05 |  |
| w16/06 |  |
| w16/07 |  |
| w17/01 |  |
| w17/02 |  |
| w17/03 |  |
| w17/04 |  |
| w17/05 |  |
| w17/06 |  |
| w17/07 |  |
| w18/01 | **Deadline!** |

## Architecture notes

Use a simple NxN matrix as a "patch bay". Pass a pointer to that matrix to each
node as a mutable reference. Nodes know their own ID.

Question: how would they know the IDs of modulators? Maybe the matrix should
not be a raw array (in a structural sense), but rather a mirror-like mapping
(axis going across the array)?

## Useful links

- [Generating Music with AI: History, Challenges, and Future Prospects](https://youtube.com/watch?v=D3XfYUUI0wc)
- [A Rust Flavored Introduction to Audio Quality Prediction](https://youtube.com/watch?v=ZTY3fqulFQ4)
- [Neural Audio Effects](https://youtube.com/watch?v=qy6qNvV1RZY)
- https://www.christiansteinmetz.com/
- [Modelling black-box audio effects](https://arxiv.org/pdf/2211.00497.pdf)
- [Quantitative Analysis of a Common Audio Similarity Measure](https://www.ee.columbia.edu/~dpwe/pubs/JensCEJ09-quantmfcc.pdf)
- [Languages for Computer Music](https://www.frontiersin.org/articles/10.3389/fdigh.2018.00026/full)
- [AudioFlux](https://github.com/libAudioFlux/audioFlux) - audio analysis toolkit
- [Riven@XXIIV](https://wiki.xxiivv.com/site/riven.html) - UI design inspiration
- [Neuroevolution of augmenting topologies](https://en.wikipedia.org/wiki/Neuroevolution_of_augmenting_topologies),
  could be interesting for keeping the graph population diverse
- [Sound comparison with MFCC](https://github.com/d4r3topk/comparing-audio-files-python)
- [Song fingerprinting - Chromaprint](https://oxygene.sk/2011/01/how-does-chromaprint-work/)
- [Rust FFT](https://docs.rs/rustfft/latest/rustfft/)
  - Learn what short term fourier transform is
- [Similar papers](https://www.google.com/search?q=genetic%20synth%20patch%20&ie=utf-8&oe=utf-8&client=firefox-b-m)
- Could be a good learning resource - works of [Curtis Roads](https://en.m.wikipedia.org/wiki/Curtis_Roads)
- [neural nets generating FM patches](https://fcaspe.github.io/ddx7/) 
- [Physical modeling using digital waveguides](https://ccrma.stanford.edu/~jos/pmudw/)
- [Mutable Instruments' Elements DSP folder in their GitHub repo](https://github.com/pichenettes/eurorack/tree/master/elements/dsp)
- https://sweetcocoa.github.io/pop2piano_samples/
- Stable Riffusion

Todo: Read the `now` entry and restructure it

## Similiar papers:

- [Automatic design of sound synthesizers as pure data patches using coevolutionary mixed-typed cartesian genetic programming](https://dl.acm.org/doi/10.1145/2576768.2598303)
- [Differentiable FM Synthesis of Musical Instrument Sounds](https://fcaspe.github.io/ddx7/)
- [ml-synth-preset-generator](https://github.com/jakespracher/ml-synth-preset-generator)
