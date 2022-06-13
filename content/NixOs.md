---
created: 2022-06-13T23:48:37+02:00
modified: 2022-06-13T23:59:16+02:00
title: NixOs
---

NixOs is a Linux distro based on a fully declarative package manager, Nix.

When they say that it's declarative, they really mean it - if you copy a `.nix` os configuration file into another machine, you'll get the exact same setup. Most of commonly used GNU/Linux utilities can be configured declaratively inside the `.nix` configuration files. Forget about storing your dotfiles in a repository, now you can store your entire system's configuration! [Here's mine](https://github.com/Wint3rmute/nixos-config). 

I am currently switching my main machine from Arch to Nix, as it solves my biggest issue with OS management, by making the whole system stateless. My main concern when experimenting with UNIX systems was that I always had to carefully keep track of all the changes I'm making, which are often scattered across different configuration files, written in different languages/formats. Even though I find the Nix language confusing at times, I believe that is has the potential to grow into a wonderful ecosystem.

Useful links:
- [NixOs egui](https://scvalex.net/posts/63/)
