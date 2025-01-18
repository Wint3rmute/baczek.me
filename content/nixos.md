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

# Tips & notes

- NixOS has excellent support for ZFS, arguably the most advanced filesystem currently on the market. [Article about ZFS on the unofficial NixOS wiki](https://nixos.wiki/wiki/Main_Page)
- Convert your system configuration into flake-based as soon as possible. It makes your system fully reproducible and makes it easier to use stuff like Agenix
  - https://wiki.nixos.org/wiki/Flakes
- Creating and maintaining custom SystemD services/timers is a breeze in NixOS
  - https://wiki.nixos.org/wiki/Systemd/User_Services
- There is a `formatter` key in Flake configuration. If you set it to a formatter program, use `nix fmt` to format your code

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
