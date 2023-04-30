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
| w10/ |  |
| w11/ |  |
| w12/ |  |
| w13/ |  |
| w14/ |  |
| w15/ |  |
| w16/ |  |
| w17   | **Deadline!** |

## Architecture notes

Use a simple NxN matrix as a "patch bay". Pass a pointer to that matrix to each
node as a mutable reference. Nodes know their own ID.

Question: how would they know the IDs of modulators? Maybe the matrix should
not be a raw array (in a structural sense), but rather a mirror-like mapping
(axis going across the array)?

## Useful links

- [Generating Music with AI: History, Challenges, and Future Prospects](https://invidious.baczek.me/watch?v=D3XfYUUI0wc)
- [A Rust Flavored Introduction to Audio Quality Prediction](https://invidious.baczek.me/watch?v=ZTY3fqulFQ4)
- [Neural Audio Effects](https://invidious.baczek.me/watch?v=qy6qNvV1RZY)
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
