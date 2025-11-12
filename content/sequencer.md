---
created: 2022-06-21T12:37:23+02:00
modified: 2022-12-18T17:49:09+01:00
title: Custom sequencer
---

## Machine Elves

Randomly stumbled around the idea of Machine Elves. I like the concept of creatures singing things into existence, even self-modifying themselves. Perhaps some elements of cellular-automata-like features could be incorporated into the sequencer? The pattern could be a structure unstable by default.

Some sort of kernel (think image processing) could be made available for the user to describe rules of self-transformation. The pattern could flip back and forth between repetitions, letting the user decide if they want to take a step forward or modify the kernel.

Ideas:

- 2D cellular automata pattern modification
- What about parameter modifications?
- How to control how radical the changes would be?

## Yet another take 2

- Base component of the program would be a cursor, moving through a board
- The cursor has some kind of internal state (a stack, a dict, whatever)
- The cursor moves through a program, which is expressed as a semi-visual programming language
  - It is on a terminal screen, like Orca
  - THe cursor can move in all directions, depending on the commands in the program

## Yet another take

I should simply rewrite Orca and add some cool midi
IN and a multiplayer mode. Sounds like a reasonable
Rusty project for a few weekends.

## New branch of ideas - interconnectivity

Image a drum sequencer in which you never directly program
patterns. Instead, you get a few "basic" rhytms and
compose complex patterns by relationships between other
patterns - addition, subtraction, xor, negation, etc. This
approach could also be applied to parameter modulation and
then used for breathing more life into melodies.

## Unordered dump of ideas for a custom sequencer

- Think tracker but scriptable in a repl-like manner
- Runes/Opcodes for sound modification
- It should be possible to "carry" packets of data around the program (like a packet of information containing a sound trigger info)
- https://blog.sbensu.com/posts/demand-for-visual-programming/
- How should if statements work?
- Song transitions, pattern muting?
- Does a minimal (opcode-centered) system allows for more better rhytmic expression than a typical programming language?
- Handling of external midi events, I want to trigger functions with the pads of my midi controller
- cursor going from top to bottom, showing some metadata on the left, while the executed code is on the right
- Loading functions from a normal text file, the sequencer runtime will listen to file changes and hot reload functions on the fly
- Labels in "pauses" so that the runtime knows where to pick up a specific function after code update? 

### Basic assumptions about the "language"

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

### Embedded scripting language?

[Crafting Interpreters](https://craftinginterpreters.com/introduction.html)

Rust has Rhai, I'm kinda eager to try it :)

Figuring a custom langauge could be a funny adventure,
I could start from some very limited Lisp implementation.

### Prototyping with snippets

#### Cool ligatures

```
|> -> => \/ ->> =>> ~> 
```
PRINT

```
seq kick 1 # Optional: set a default MIDI channel
pattern_select -> @2.73 # Define a midi listener. Channel 2 message 73
pattern = [ 'C3! C3! C? C G G! ]  # Define a seq-scoped variable
step = 0

rhytm:
pattern [step]  # Expression returning a value sends it via midi
step += 1
step %= 1
> 1 rhytm  # Await a single step and jump to rhytm:
```

- It should work in multiple directions, right to left, left to right, etc. If Opcodes are just 1 letter long, it won't be a problem to read right-to-left or bottom-to-top
- A language server should be defined separately from the server, so I can later write something like `neovide` for it
