---
created: 2022-06-13T23:48:37+02:00
modified: 2022-10-27T22:56:27+02:00
title: NixOs
tags: programming, collection
---

NixOs is a Linux distro based on a fully declarative package manager, Nix.
Forget about keeping a script for setting up your system or storing your
dotfiles in a repository, Nix will take care of it.

I am currently using NixOs on my server/homelab infrastructure. From my
experience so far, it is a step up from Ansible playbooks or similar tools. I
am reluctant to switch my main laptops to NixOs, as it's not as easy to program
on NixOs as it is to deploy software on it. Hopefully this will change in the
future :)

Useful links:

- [VimJoyer YouTube channel](https://youtube.com/@vimjoyer) - high quality Nix tutorials
- [Nix-ld](https://github.com/Mic92/nix-ld) - running "normal" binaries on NixOs
- [An overview of Nix in practice](https://www.slice.zone/blog/nix-in-practice)
- [MyNixOs](https://mynixos.com/) - comfy search engine for NixOs configuration
  options
- [NixOs egui](https://scvalex.net/posts/63/)
- [Nix Pills](https://nixos.org/guides/nix-pills/)

Tips:

- NixOS has excellent support for ZFS, arguably the most advanced filesystem currently on the market. [Article about ZFS on the unofficial NixOS wiki](https://nixos.wiki/wiki/Main_Page)
