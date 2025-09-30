---
created: 2025-09-02T11:01:19+02:00
modified: 2025-09-02T11:08:25+02:00
title: Model-Based Systems Engineering
tags: programming, engineering
---

My observations & ideas on tooling for [Systems Engineering](https://en.wikipedia.org/wiki/Systems_engineering)
and [Model-based Systems Engineering (MBSE)](https://en.wikipedia.org/wiki/Model-based_systems_engineering).

For a prototype tool for markdown-driven requirements management, see
[ReqSnake](/reqsnake).

## Problem statement

We lack tools for system modeling, which can validate both low and high-level
system model, allow placing useful constraints on the model, running tests on
the model; not merely diagramming a bunch of blocks and arrows. Existing tools
are stuck in a hell of desktop GUI apps with license servers and other typical
issues related with large corporate software.

While programming tools get better, compilers get smarter and linters get
stricter, **we're still representing knowledge about systems using documents
with screenshots of hastily sketched DrawIO diagrams**. Time to put an end to
the tyranny of the underspecified and the tribally-known! Release the system
model & knowledge from the restraints of pre-hypertext mediums.

Embrace the [rhizomatic](https://en.wikipedia.org/wiki/Rhizome_%28philosophy%29) and the gradually-typed! Hyperconnect and hypervalidate!

Let's model systems like it's XXI century AD.

## Solution statement

Build a system which joins together:

- Knowledge management in a form of a interconnected network
- System modelling tool with a focus on connections:
  - Protocols
  - Interfaces/ports
  - Encapsulation
- System exploration tool with an interactive diagram generator

## 💢 Core issues

### GUI

GUI-based tools don't scale and give a false sense of simplicity, which causes
explosion of complexity each time a non-trivial system has to be modeled. GUIs
are perfect for **exploration**, but they tend to be lacking for **structured
and disciplined creation**, which is absolutely required when exercising proper
SE.

**Conclusions:**

- the system shall generate GUI-based views or even interactive system
  exploration tools
- the system shall feature code-first system model editing

### Points of interest

From what I've seen, SE tools tend to mix together too many contexts into a
single box, often with wildly different abstraction levels. Proper separation
of business and engineering concerns is a thing of rigor, but the tool at hand
often affects the craftsman, leading to more or less organized result. The end
user should be able to filter out the things they have no interest in, only
viewing the context relevant to them.

**Conclusion:** the system shall implement definable _Views_, which would
essentially be filters applied onto the system model.

**Possible extension:** perhaps the whole thing could work as a graph database
with a query engine, allowing the user to programically sculpt their view of
the system?

```python
>>> find("#Phone").interfaces_with(find("#SocialMedia"))
"""
┌────────────────────┐  ┌────────────────────────┐
│ Phone              │  │ SocialMedia            │
│                    │  │                        │
│  ImageInGallery─┐  │  │                        │
│                 ├──┼──┼─►PostCreationInterface │
│  SocialMediaApp─┘  │  │                        │
│                    │  │                        │
│  NotificationBar◄──┼──┼──NotificationService   │
└────────────────────┘  └────────────────────────┘
"""

>>> find("#Phone").interfaces_with(find("#CellPhoneTower"))
"""
┌────────────────────┐  ┌────────────────────────┐
│ Phone              │  │ CellPhoneTower         │
│                    │  │                        │
│  CellularModem◄────┼──┼─►Antenna               │
└────────────────────┘  └────────────────────────┘
"""
```

**Note**: The app would render pretty interactive diagrams in reality!

## 💡 Ideas

### Fully Defined

From the [OnShape forums](https://forum.onshape.com/discussion/25425/what-does-fully-defined-mean):

> The short answer is that 'fully defined' means you have told the program
> explicitly how to calculate the position of every point, line, arc etc. which
> exists in your sketch when changes are made to the model.

This concept can be useful in terms of MBSE. During prototyping
phase, one might define some kind of information to be sent from a system to
system, for example a `User` of a `SocialMedia` might want to send information
of type `Image` from their `Phone` to the `SocialMedia`. Such relationship can
be easily understood by high-level executives. It is valid in the business
sense, **but not in engineering sense**. It is therefore not _fully defined_.
The system shall still allow business people work in high-level concepts, but
once an architect or an engineer sits down to determine the details, the system
should point out the missing pieces: request formats, protocols, etc.

**Conclusion:** The system shall support something similar to [Gradual
typing](https://en.wikipedia.org/wiki/Gradual_typing) of the model, allowing
engineers to switch between different strictness levels of coherency checking.

### Thorough interfaces/ports modelling

In software projects, information flows often in non-trivial ways. Some
domain-specific entity is encoded as JSON, sent over a Message Queue, goes into
a microservice which performs validation and lands in a database at the end.

I would like to check if some domain-specific entity will be able to **reach**
the desired recipient through the defined structure of interfaces and
connections. Perhaps someone mistakenly plugged in the frontend directly into a
database? The modeling tool should catch that error and raise
a `IncompatibleInterfaceException`.

### Permission model

A large/confidential/military system model will require permissions for
accessing some of its parts. A "throw it all into a single Git repo" approach
will not cut it. Instead, I suggest a 2-way approach:

- Define system parts as _modules_ or _packages_, like a programming language
- Allow for parts of the system to be imported from git repos:
  - Submodule
  - Via clone URL + hash/tag/branch, see how [Cargo does it](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html)

### Lockfiles

See [ReqSnake](/reqsnake).

## ❓ Known Unknowns

### SysML

This standard looks like a PITA. Take a look at [the spec](https://sysml.org/sysml-specs/).
Compare it to documentation of any sane programming language, file format or
communication protocol. SysML, have mercy on me!

## 😨 Unknown Unknowns

### Systems/Models/Setups

Approach to re-using the same system in multiple setups. E.x modeling the same
project in both end-user and testing environment.

### Gradual typing

How should this be expressed at the system-as-code level? Some interface should
be marked as "abstract" while other as "base-level" or "physical"?

Maybe do something like first-degreee requirements (completely high-level,
product idea type), then second-degree, then (...) N-th degree as something
that's finally "solid" and "physical", whatever that means in a context of a
specific system.

# Existing tools

- https://www.jamasoftware.com/
- https://www.genesys.com/en-gb
- https://www.reqview.com/
- https://mbse-capella.org/
- https://www.sysgit.io/
- https://gaphor.org/
- https://www.ibm.com/docs/en/engineering-lifecycle-management-suite/doors/9.7.2?topic=engineering-requirements-management-doors-overview
- https://sysmodeler.ai/home
