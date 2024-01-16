---
created: 2022-10-27T23:13:55+02:00
modified: 2023-04-25T22:05:57+02:00
title: Software alternatives
tags: programming, collection
---

Here's a small list of programs which I use as alternatives to classic
UNIX-related tools. Lesser-known first to keep the list interesting:

- [LeftWM](https://leftwm.org) - a window manager
- [Helix](https://helix-editor.com/) - a text editor
- [Zellij](https://zellij.dev/documentation/overview.html) - `tmux` alternative, batteries included
- [Nu](https://www.nushell.sh/) - cross-platform shell with a fresh approach to streams & redirections 
- [Zola](https://www.getzola.org/documentation/getting-started/overview/) - a static site generator, which powers this website
- [Paru](https://github.com/Morganamilo/paru) - AUR helper for all Arch folks
- [Neovide](https://neovide.dev) - `neovim` client with eye-candy animations
- [Caddy](https://caddyserver.com/) - a web server with automatic HTTPs and refreshingly simple configuration
- [Alacritty](https://alacritty.org/) - a terminal emulator
- [Wezterm](https://wezfurlong.org/wezterm/) - another terminal emulator
- [fd](https://github.com/sharkdp/fd) - unix `find` but actually usable without having to read `man` each time

---

I encourage you to compare the listed softwares
with their more classic alternatives in terms of documentation, contribution
guides and CI/CD practices.

# Justification/Philosophy

Most of the software that powers our devices runs on C, C++ and Java. I do not
mean to criticise those languages, as they were (and still are) a great
improvement for the programming community, opening new and exciting paths to
better software. However, during the last 2 decades, new languages have
emerged, fulfilling the need for:

- Built-in tools for easier code reuse (package/library management)
- Memory safety
- Performance & resource usage efficiency
- Improved approach to macros, code generation and other
  metaprogramming-related aspects
- Stronger & more expressive type systems
