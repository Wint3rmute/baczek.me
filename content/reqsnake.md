---
title: ReqSnake
tags: programming, project
---

# Requirements Management System

[ReqSnake](https://github.com/Wint3rmute/ReqSnake) is a small script for
managing project requirements, which I created in Python over the course of ~10
afternoons. I created ReqSnake for 2 core reasons:

- I despise currently existing requirements management software
- I wanted to experiment with agent-based coding

## Intro to Requirements Management

Working in the space industry, I have some experience with [Systems
Engineering](https://en.wikipedia.org/wiki/Systems_engineering). The core idea
behind Systems Engineering is building a layer above domain-specific engineers:
mechanical, electronics, programming, **while still remaining
technology-oriented**, rather than business-oriented. There should be someone
who will understands the whole thing on a high-level, operating on a different
layer of abstraction, concentrated on the overall system rather than on one of
its many parts.

If you're reading this, you're probably used to the tools like
[Jira](https://www.atlassian.com/pl/software/jira) and have heard about [User
Stories](https://www.atlassian.com/agile/project-management/user-stories).
Project Requirements in the Systems Engineering jargon are something which is
placed between User Stories and the actual work to be done by domain-specific
engineers. A client defines what they want to get, System Engineers work with
the client to build understanding of what exactly should be built. For
simplification, we can assume that Systems Engineers write this down together
with the client as User Stories, althought they might use different tools.
What's important is that after building a mental model of what the user wants,
Systems Engineers distill it down into **Project Requirements**.

While User Stories work perfectly fine in software-only environments, the
complexity of interdisciplinary projects requires an additional layer of
abstraction, in the form of Project Requirements. They are more formalized and
more technical than User Stories. In an ideal world, each requirement should be
veryfiable in a quantitative way. E.x:

> The USB port should be capable of transferring data at rate no smaller than 1.5Mbit/s.

This is something which you could easily test by running a benchmark on the
developed machine. Unfortunately, end-clients don't always operate at such low
abstraction layers, they might think about it like this:

> The camera should have a USB port and it should transfer the entire contents
> of camera's storage onto a computer in no longer than 10 minutes.

This is where **Requirements Breakdown** comes in.

### Breaking it down

High-level requirements, usually describing high-level attributes of a final
product, are broken into child requirements. This is similar to breaking down
User Stories into managable tasks, although with a bit more formalities and
rigor. There usually are multiple layers of child requirements. A project-wide
requirement may be first broken into multiple stages according to the project
timeline, then it might be split between engineering teams, then across
multiple domain experts in a specific field. Continuing with the example
requirement about camera's USB port:

**1. First, project timeline:**

- High-priority, to be done early on. For the electronics and mechanical departments:

  > The main PCB board shall host a USB connector

- Low priority, to be done later. For the technical writers or marketing:

  > The user manual shall feature a section about a USB connector

**2. Then, split between engineering teams:**

- Software:

  > The camera's SoC shall support USB peripherals

- Electronics:

  > The camera's SoC shall be connected to the USB peripheral

**3. Afterwards, split between domain experts:**

- Software, embedded Linux:

  > The kernel shall support USB peripherals, acting as a USB gadget

- Software, UI:

  > The Camera UI shall react to plugging in the USB cable by entering displaying a dialog

What's important is the process of **linking** requirements into a logical
hierarchy, with project-wide requirements at the top and domain-specific
requirements at the bottom.

### Tracing

The links between high-level and low-level requirements establish a logical
structure, justifying each low level requirement in terms of high-level ones.
There should always be an answer to _"why are we building this specific piece
of hardware/software?"_, and it should be possible to find that answer by going
**up the hierarchy** of requirements.

### Verification activities

Once the final hardware (or it's first development versions) are built and
delivered to a testing facility, the requirements shall also define
verification activities, which would verify compliance to each low-level
requirements. Based on low-level compliance, requirement tracing allows to
determine which higher-level requirements are met by a set of low-level tests.
The same approach is used all the way up to project-wide requirements.

### Auditing

The client may want to audit the company building the product. The audit
process often requires sharing the requirements management system with the
client or a separate auditing company. The hierarchy of requirements is a base
for justifying activities performed by engineers and a sign of how competent
the company's architects are at breaking down project requirements into smaller
activities.

### Change control

When building a different version of a product (another revision, or a build
tailored to a specific client), the hierarchy of requirements allows Systems
Engineers to figure out how changes at the top of the hierachy affect different
engineering departments. This allows them to predict costs of specific changes
more precisely than when relying solely on experience/intuition, leading to
better decisions.

### Summing up

By now you should have a high-level grasp on Systems Engineering and
Requirements Management. Systems Engineering is all about breaking down a
complex system into a series of sub-systems. It is also about knowledge
management - determining which parts of system-wide requirements should be
passed along into which engineering team.

Requirements Management is meant to make it easier for Systems Engineers to do
their work, providing a formalized framework where requirements are defined and
broken down into domain-specific child requirements. The breakdown process
links different abstraction layers together, providing a hierarchical structure
of knowledge, which defines the final product to be built, as well as steps of
validating that the product meets clients' criteria.

## What's on the market

Huge, proprietary systems. Some big names:

- IBM Doors
- Enterprise Architect
- Jama Connect

My biggest complaint about those systems is that they force the company into a
typical corporate workflow.

1. There is a huge application that is so complex that it requires weeks of
   introductions to get around.
2. The application has a costly license. It takes a long time to get the
   license for the new employee.
3. The application is a pain to integrate with any external systems. The
   company building the application actively discourage any kind of
   integrations, as they want to make money from their own solutions. If you ever
   interfaced with any kind of large corporate API, you know the pain.
4. It is nearly impossible to migrate to a different system, as everything is
   closed behind proprietary file formats.
5. The company **no longer owns their documentation and requirements**.
   Instead, they are hostages to how the 3rd party Requirements Management
   system is built.

Instead, a good tool should:

- Integrate with open formats
- Be easily extendable
- ...ideally be free and open source?

## Designing a solution

Personally, I think about Requirements Management as a subset of _knowledge
management_. Just as documentation contains knowledge about the product,
Project Requirements are a formalized part of the documentation. Due to
tracing, they must be structured and hierarchical. So:

- Extend existing documentation
- Use an open format used to write documentation

To no one's surprise, the clear winner here is Markdown. I don't have any
official statistics, but the majority of the libraries I use have their
documentation written in this simple markup language. There are tons of
Markdown tooling, generating static websites with explorable documentation.

And so the choice was made, I wanted to extend existing Markdown documentation
with a bit of extra syntax to define requirements.

I settled down on the following blockquote-based syntax:

> CORE-1
>
> The camera shall feature a USB port.

---

> SOFTWARE-1
>
> The kernel shall support USB peripherals.
>
> child-of: CORE-1

The premise is simple:

1. Install my requirements management tool.
2. Extend your existing documentation with blockquote-based requirememnts
   definitions.
3. You are a Systems Engineer now!

### Features

As of now, ReqSnake provides the following functionalities.

#### Documentation scanning

ReqSnake will scan a specified folder for Markdown documents and extract
requirements definitions from them.

#### Dependency verification

You can only make a requirement as completed once all of its child requirements
are completed. ReqSnake will raise errors if you try completing a requirement
with non-completed child requirements.

#### Report generation

You can generate a report with the current status of the requirements. A
Markdown report is the core functionality here, although printing directly to a
terminal is also available. I'm also working on Graphviz output, although it is
very much work in progress now.

#### Chage tracking

Markdown documentation is usually tracked with `git`, so a lot of change
control is already there. However, when actively working on the changes, it is
possible to get a summary of modified requirements.

For this mechanism to work, I implemented a `reqsnake.lock` file, similar to
`Cargo.lock` or `poetry.lock`. The file should be regenerated each time when
requirements are changed. This can (and should be) be integrated into a CI/CD
pipeline.

#### Easy to extend Pythonic API

Instead of using the CLI, you can simply import ReqSnake's core functions to
Python and operate on them for any kind of extra processing. Examples available
in the [repository](https://github.com/Wint3rmute/ReqSnake).

#### Zero dependencies

A recent Python3 installation is all that's needed to work with ReqSnake. In
theory, one could simply fetch the script from GitHub and be good to go.

## Agent-based implementation

**Note:** This part will be focused on the **implementation** of the
application. No need to read if you're only interested in the functionalities.

I wanted to use AI-assised coding for something useful. From what I've read on
the internet, this project has the right size and complexity. Additionally, I
wanted to do a cool trick: write ReqSnake requirememnts first and manage them
with ReqSnake itself. Adding an AI agent implementing ReqSnake at the same time
adds another recursive element to the mix. Additionally, guides on AI agents
usage encourage writing rich documentation for the agents to use. Requirements
specification, broken down into module-specific requirements, sounds like a
perfect reading material for an AI agent.

### Tools

Cursor free tier. No extensions. Default prompts.

### Starting out

The beggining always goes smooth with AI. I scribbled down requirements
regarding the overall goal of the software, the blockquote format to use and a
simple description of CLI commands to be available. I got a working prototype
within minutes. **I proactively stopped myself from looking at the generated
code, trying to think about the task as a delegation problem.**

### Testing strategy

After the first prototype, I added requirements regarding testing. I specified
2 kinds of tests:

- Unit test, nothing fancy
- Integration tests (i called them "scenario tests")

Scenario tests create a temporary directory, write some Markdown into the
directory, then use the Python interface of SnakeReq to call functions and
validate returned results.

The AI implemented both kinds of tests. In hindsight, starting scenario-based
testing as early as possible was the biggest lifesaver. It's no surprise, the
same is true for non-vibecoded projects.

### What the AI got right

#### ✅ CLI interface

`argparse`-based CLI was generated without any specific hints, just a broad
description. Makes sense, CLI is a common thing to write.

#### ✅ Lockfile generation

Not so common use-case, but it boiled down to serializing a bunch of
`dataclass` objects to a JSON. Nice to see it work.

#### ✅ Tests generation

I haven't thoroughly reviewed them, but there are around ~50 tests so far. They
seem to be doing a good job, as they frequently go off when the AI is
refactoring anything. More tests to come.

#### ✅ Tool usage

Apart from unit tests, I also set up:

- Ruff for linting and docstring checking
- Mypy with strict settings

All lints/tests can be run with `./check.sh` script, which I added to the
system prompt of the agent. The agent had no issues with using the script and
interpreting the output of those tools, usually taking 3-5 iterations to get
the solution right. It was somewhat satifying to see it figure out the issues.
It was even more satisfying to look outside the window or drink tea while the
model was working. Cursor can be configured to generate an audio bell once the
model indicates that it has finished, I highly recommend this option.

#### ✅ Fun with recursion

As AI is good at generating formal sounding text, I usually prompted it like this:

> I want to add a new requirement: **briefly and non-formally describe the requirement**.
>
> 1. Write down the requirement, link it into the context of already existing requirements.
> 2. Implement the requirement in code.
> 3. Implement tests for the new code.

This was a suprisingly satifying combo, as the model was able to:

1. Make a plan of what to do
2. Formalize it into a requirement
   - The requirement can be useful later as context/documentation
3. Implement both the code and the tests
4. Run the aforementioned `./check.sh` and iterate a couple times

#### ✅ CLI UX, status and error messages

CLIs are nice when they generate recognizable messages. I very much enjoyed typing in:

> Add emojis to all messages which you print to the user in the CLI

And getting a sensibly chosen emojis in outputs. Quality of life change,
effortless to add.

---

This got me to a point where I could run:

1. `./reqsnake.py init` to bootstrap requirements tracking in a project.
2. `./reqsnake check` to see changes between the lockfile and the current
   state of requirements.
3. `./reqsnake.py lock` to save requirememts changes into a lockfile.
4. `./reqsnake.py status` to print defined requirememts into the terminal.
5. `./reqsnake status-markdown` to generate a Markdown report with status of requirements.

### What the AI got slightly wrong

#### ⚠️ Dependency cycle detection

Despite specified requirements, the agent **completely ignored** my
instructions regarding cycle detection. When asked about it, it responded that
it is in fact not implemented and quickly coded a DFS. It seems to be working,
although it requires more tests at this point. I'm counting this as slightly wrong.

#### ⚠️ Blockquote parsing

To my surprise, AI did not understand the idea behind making a specific
blockquote-based syntax for requirement definitions. It assumed that **all
blockquotes** in the documentation shall be valid requirememnts. I had to
pinpoint this fact then the AI implemented a somewhat sloppy heuristic deciding
when to raise an error and when to assume that the blockquote definitely does
not contain a requirement. Only time will tell whether this heuristic is
correct. Again, slightly wrong.

### What the AI got completely wrong

#### ❌ Multiline strings

Honestly, this was the biggest surprise for me. As most mature languages,
Python has decitated syntax for multilines strings:

```python
long_string = """Hello
So basically
I am very long.
"""
```

This looks like a perfect solution for writing scenario tests. Markdown files
can be written within the test code as multiline strings, then written to
files, then be used to check ReqSnake functions. For some reason, AI generated
everything as unreadable single-line strings with `\n` characters.

```python
long_string = "Hello\nSo basically\nI am quite unreadable."
```

What's weird is that it **could not convert** between those 2 formats properly.
It kept on breaking unit tests and running into syntax errors. I left my
computer for 10-15 minutes and it did at least a dozen of iterations, failing
every time. I gave up and refactored the thing myself in 5 minutes.

Afterwards, AI kept on generating new test casesusing single-line strings. IMO
this is a big issue, because as the test suite grows, the unreadability of
markdown squashed into single lines is going to add up.

#### ❌ Code structure, DRY, and similar

I'm not a DRY apostle by any means. Bad repetition is better than bad
abstraction. However, there are clear cases when defining a suite of reusable
functions is a clear win. Any kind of parsing and validation logic are such
case. Despite this, the AI kept spitting out similar looking snippets for
validation of requirements, reading the lockfile, etc.

I gave it a few tips, thinking my prompting is wrong:

- I wrote repetitive unit tests, excercising the same functionality with
  different CLI commands
- I asked the AI if it can find repetitive code in the parsing logic
- I asked the AI to act as a Python expert and suggest improvements

I observed similar behavior in each case. The AI could **tell me** that there
is repetition. In fact, it described the location of the repetition quite
precisely. Unfortunately, it could not effectively eliminate the repetition. It
could only build layers above the tools it had already generated, not think
about how the existing tools could be modified or consolidated better align
withh the overall code structure.

The funniest case was when I suggested to apply the DRY principle to the
parsing logic, the AI happily said that it understands the issue, then it
generated **even more duplicated code** and claimed to have improved code
quality and robustness.

## Observations

### Human work

My key takeaway from this project is that AI can relieve me of mental overhead
when working on small tools. The afternoons spent on ReqSnake were much less
demanding than typical programming. I could do other things and I felt less
tired after a ~2 hour session.

### Documentation shines

I picked a project where requirements specification was key. I was a good
decision. AI frequently cited existing requirements in responses and used them
as additional context. The formal and terse nature of requirements might be a
key factor to their effectiveness in the context of agentic coding.

### Feedback is key

Tools, linters, tests. There was virtually no case when my stupid simple
`./check.sh` script wasn't useful for the agent. In fact, I think it was the
only thing preventing the project from collapsing down on itself after reaching
1k+ LoC.

### Summing up

AI agents are no different from humans in the case of specifying programming
work to be done. High quality documentation and a short feedback loop by
automated testing and lints are what saved the AI multiple times from
introducing regressions or low quality code.

There are still many issues regarding code duplication and the inability to
deeply refactor existing tools. An experienced developer still has to set up
project-specific linting & testing policies, although I believe that this can
be easily automated by project templates.

I would like to see those tools progress to a point where I can delegate tasks
as if I was talking to mid-level programmers. Even more intelligence would of
course be nice, but this would be too much speculation.
