---
created: 2022-06-21T12:37:23+02:00
modified: 2022-11-20T21:55:59+01:00
title: Custom sequencer idea dump
---

## Unordered dump

- Think tracker but scriptable in a repl-like manner
- Runes/Opcodes for sound modification
- Do I need math operators like in orca?
- It should be possible to "carry" packets of data around the program (like a packet of information containing a sound trigger info)
- How should if statements work?
- Song transitions, pattern muting?

## Basic assumptions about the language

A language which can move arbitrary lists around..? 

## Crazy ideas dump

- It should work in multiple directions, right to left, left to right, etc. If Opcodes are just 1 letter long, it won't be a problem to read right-to-left or bottom-to-top
- A language server should be defined separately from the server, so I can later write something like `neovide` for it
