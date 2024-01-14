---
created: 2022-06-13T23:48:37+02:00
modified: 2022-10-27T22:56:27+02:00
title: NixOs
tags: programming, collection
---

NixOs is a Linux distro based on a fully declarative package manager, Nix.

When they say that it's declarative, they really mean it - if you copy a `.nix`
os configuration file into another machine, you'll get the exact same setup.
Most of commonly used GNU/Linux utilities can be configured declaratively
inside the `.nix` configuration files. Forget about storing your dotfiles in a
repository, now you can store your entire system's configuration! [Here's
mine](https://github.com/Wint3rmute/nixos-config). 

I am currently switching my main machine from Arch to Nix, as it solves my
biggest issue with OS management, by making the whole system stateless. My main
concern when experimenting with UNIX systems was that I always had to carefully
keep track of all the changes I'm making, which are often scattered across
different configuration files, written in different languages/formats. Even
though I find the Nix language confusing at times, I believe that is has the
potential to grow into a wonderful ecosystem.

Update: unfortunately, due to lack of documentation I had to abandon Nix, as I
was spending more time writing the configuration required to build my software
than the actual software itself. If I was doing just web development, Nix would
be a perfect match for me. I still see great potential in the project, I'll
definitely come back to Nix in a few years.

Useful links:

- [An overview of Nix in practice](https://www.slice.zone/blog/nix-in-practice)
- [MyNixOs](https://mynixos.com/) - comfy search engine for NixOs configuration
  options
- [NixOs egui](https://scvalex.net/posts/63/)
- [Nix Pills](https://nixos.org/guides/nix-pills/)
