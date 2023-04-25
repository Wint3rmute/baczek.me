---
created: 2022-07-29T12:33:09+02:00
modified: 2023-04-18T04:13:34+02:00
title: 'Synth Patch Generation - Evolutionary Approach'
tags: culture, programming, generative
---

| Week & month | Goal |
| :-- | :-- |
| w1/02 | Test FFT algos in rust, try plotting them in real time in UI |
| w2/02 | Prepare **any** prototype of synth graph building UI |

## Architecture notes

Use a simple NxN matrix as a "patch bay". Pass a pointer to that matrix to each node as a mutable reference. Nodes know their own ID.

Question: how would they know the IDs of modulators? Maybe the matrix should not be a raw array (in a structural sense), but rather a mirror-like mapping (axis going across the array)?

## Useful links

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


# Random notes in polish for uni

Zastosowanie algorytmów genetycznych do budowy grafu reprezentującego szereg algorytmów DSP,
syntezujących zadany dźwięk. Analiza hiperparametrów krytycznych dla skuteczności algorytmu.

Zakres prac:

1. Napisanie aplikacji pozwalającej na dynamiczne budowanie grafów DSP i odsłuch generowanych przez nie dźwięków.
  Podobne istniejące już aplikacje (umożliwiające jedynie **ręczną** budowę grafów):
  - [Pure Data](http://puredata.info/)
  - [Bespoke Synth](https://www.bespokesynth.com/)
  - [VcvRack](https://vcvrack.com/)
2. Wykorzystanie algorytmu genetycznego do automatycznego wygenerowania grafu DSP syntezującego wybrany przez użytkownika dźwięk
3. Porównanie skuteczności algorytmu w zależności od:
  - zastosowanej funkcji kosztu:
    - [MFCC](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum)
    - Porównanie wykresu [spektrum audio w czasie (waterfall)](https://en.wikipedia.org/wiki/Waterfall_plot)
    - Algorytmy do fingerprintingu audio: [Chromaprint](https://oxygene.sk/2011/01/how-does-chromaprint-work/),
      inne rozwiązania opisane w [Computer vision for music identification](https://ieeexplore.ieee.org/document/1467322)
  - różnego podejścia do generowania grafu (parametry algorytmu genetycznego,
    użycie [NEAT](https://en.wikipedia.org/wiki/Neuroevolution_of_augmenting_topologies), jestem w trakcie szukania
    badań, w których wykorzystywano jakąś formę automatycznego generowania grafów, żeby się zainspirować)


Prace o podobnej tematyce:

- [Automatic design of sound synthesizers as pure data patches using coevolutionary mixed-typed cartesian genetic programming](https://dl.acm.org/doi/10.1145/2576768.2598303)
- [Differentiable FM Synthesis of Musical Instrument Sounds](https://fcaspe.github.io/ddx7/)
- [ml-synth-preset-generator](https://github.com/jakespracher/ml-synth-preset-generator)
