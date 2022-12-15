---
created: 2022-06-21T12:37:23+02:00
modified: 2022-11-20T21:57:52+01:00
title: Custom sequencer idea dump
---

## Unordered dump

- Think tracker but scriptable in a repl-like manner
- Runes/Opcodes for sound modification
- It should be possible to "carry" packets of data around the program (like a packet of information containing a sound trigger info)
- How should if statements work?
- Song transitions, pattern muting?
- Does a minimal (opcode-centered) system allows for more better rhytmic expression than a typical programming language?

## Basic assumptions about the language

A language which can move arbitrary lists around..?

Idea: All "song code" should share a common variable namespace, which could be mutated
at any point (in a synchronous manner). *Edit:* this is cool but what if I want
to reuse a function? Maybe there should be a stack-based scope for the namespace?

The code defines when to tick (with something like a generator or an async/await syntax)
and a runtime makes sure that it will tick at the right time.

Each function can be hot-swapped without having to reinitialise variables, as variables 
are global. Sounds kinda crazy but this could actually be done very easily with
an embedded python interpreter.

Define short operators for doing basic sound manipulation such as
shifting by an octave, doubling in length (LilyPond syntax to the rescue?).

**I'll need to figure out some way to do smooth parameter automation though.**

## Embedded scripting language?

Rust has Rhai, I'm kinda eager to try it :)

Figuring a custom langauge could be a funny adventure,
I could start from some very limited Lisp implementation.

## Crazy ideas dump

- It should work in multiple directions, right to left, left to right, etc. If Opcodes are just 1 letter long, it won't be a problem to read right-to-left or bottom-to-top
- A language server should be defined separately from the server, so I can later write something like `neovide` for it
