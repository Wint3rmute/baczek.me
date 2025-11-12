---
created: 2022-06-13T23:48:37+02:00
modified: 2022-10-27T22:56:27+02:00
title: NixOS
---

[NixOS](https://nixos.org/) is a Linux distro which follows a path radically
different from Ubuntu/Fedora/Arch/Gentoo, etc. The system configuration is no
longer a stateful, imperative process. Instead, you describe your system using
the Nix configuration language and a fresh _system generation_ (something like
a system image) is built and activated each time you're making a change to the
system.

Simplifying, you can think about it as getting a completely fresh system on
every change, except the directories when data is kept: `/home`, `/var`, `log`.

What does that mean in practice? Forget about keeping a script for setting up
your system or your dotfiles. Forget about clearing up old configuration files.
No more conflicts between package versions. If you have multiple machines,
treat them like build configurations in programming languages and freely reuse
modules with configuration. Same users on multiple systems? Done. Same
configuration for a specific service/app? Done!

From 2023, I have been using NixOS for my server/homelab infrastructure. It is
a step up from Ansible playbooks, I even dare to say that it's a paradigm
shift. I am reluctant to switch my main laptops to NixOS, as it's not as easy
to program on NixOS as it is to deploy software on it. Hopefully this will
change in the future :)

Useful links:

- [search.nixos.org](https://search.nixos.org/) - search engine for NixOS
  configuration options
- [Nix Pills](https://nixos.org/guides/nix-pills/)
- [VimJoyer YouTube channel](https://youtube.com/@vimjoyer) - high quality Nix
  tutorials
- [An overview of Nix in practice](https://www.slice.zone/blog/nix-in-practice)
- [Nix-ld](https://github.com/Mic92/nix-ld) - running "normal" binaries on
  NixOs
- [Nix Phd thesis from Eelco Dolstra, the author of
  Nix](https://edolstra.github.io/pubs/phd-thesis.pdf)
- [NixOs egui](https://scvalex.net/posts/63/)

# Tips & notes

- NixOS has excellent support for ZFS, arguably the most advanced filesystem
  currently on the market. [Article about ZFS on the unofficial NixOS
  wiki](https://nixos.wiki/wiki/Main_Page)
- Convert your system configuration into flake-based as soon as possible. It
  makes your system fully reproducible and makes it easier to use stuff like
  [Agenix](https://github.com/ryantm/agenix)
  - https://wiki.nixos.org/wiki/Flakes
- Creating and maintaining custom SystemD services/timers is a breeze in NixOS
  - https://wiki.nixos.org/wiki/Systemd/User_Services
- There is a `formatter` key in Flake configuration. If you set it to a
  formatter program, use `nix fmt` to format your code

## Switching configurations with confidence

My homelab consists of a VPS with a static IP and a server at my place. If I
mess something up with the networking configuration (which happened more than I
initially thought), I might break the VPN configuration to my homeserver. This
would be far from perfect when I'm away from home as I'm unable to log in
locally and fix the networking configuration.

I didn't want to install something like [Tailscale](https://tailscale.com/) or
[ZeroTier](https://www.zerotier.com/) ~~because I'm a purist~~ because it's my
homelab and I wanted to be independent!

The deployment procedure has been working for me for over 2 years and survived multiple configuration mishaps:

1. Run `nixos-rebuild build` before you make any modifications
2. Schedule a reboot in 15 minutes
3. Run `nixos-rebuild test`
4. Run VPN connectivity tests (simple pings via some script or via `ansible`)
5. Cancel the scheduled reboot
6. Run `nixos-rebuild switch`
