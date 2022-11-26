---
created: 2022-07-29T12:33:09+02:00
modified: 2022-08-24T19:55:43+02:00
title: Synth Patch Generation - Evolutionary Approach
---


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


---

Yada yada następujące zagadnienia:

1. Silnik DSP:
  - Synteza dźwięku - algorytmy [syntezy FM](https://ccrma.stanford.edu/~jos/sasp/Frequency_Modulation_FM_Synthesis.html) oraz [physical modeling](https://ccrma.stanford.edu/software/clm/compmus/clm-tutorials/pm.html)
  - Filtracja dźwięku - [algorytmy emulujące klasyczny filtr analogowy](https://ccrma.stanford.edu/~jos/filters/Elementary_Audio_Digital_Filters.html) - rezonansowe high-pass, low-pass, emulacja klasycznego *moog ladder filter*
  - Przetwarzanie gotowych sampli:
    - Zmiana wysokości dźwięku
    - [Bit crush sampli](https://en.wikipedia.org/wiki/Bitcrusher)
    - [Distortion/overdrive](https://en.wikipedia.org/wiki/Distortion_(music))
  - Efekty audio, nakładane na sample i syntezowane sygnały dźwiękowe:
    - Reverb - przykładowo [Dattorro’s figure-of-eight reverb](https://ccrma.stanford.edu/~dattorro/EffectDesignPart1.pdf) lub [freeverb](https://ccrma.stanford.edu/~jos/pasp/Freeverb.html)
    - [Delay](https://en.wikipedia.org/wiki/Delay_(audio_effect)), emulacja efektu tape delay
2. [Sequencer](https://en.wikipedia.org/wiki/Music_sequencer) - komponent pozwalający na zaprogramowanie przez użytkownika:
  - Rytmu/melodii odgrywanej przez silnik DSP
  - dynamiczne zmiany wartości parametrów syntezy oraz przetwarzania dźwięku opisanych wyżej
  - Rytmu/melodii odgrywanej na zawnętrznym kanale MIDI (w celu integracji z instrumentami zewnętrznymi: pianino elektroniczne/syntezator/itd)
3. Interfejs użytkownika:
  - Ustawianie parametrów silnika DSP
  - Podgląd i edycja rytmów/melodii w sequencerze

