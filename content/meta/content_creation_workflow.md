---
created: 2022-05-01T23:43:57+02:00
modified: 2022-05-02T00:03:47+02:00
title: Content creation workflow
---

# A starting point

Here's a bunch of opinions I have on writing and storing notes/ideas/etc:

- it's always good to be able to make notes, drafts or even full pages from your phone. It feels good to use a smartphone for something other than content consumption.
- CI/CD or other repository automation is a good idea, no matter what project you're working on.
- Use git to store your content, use any other tool you like for viewing/writing/visualisation.
- Markdown is most probably all you need. Remember that you can always extend markdown - almost all static site generators allow you to spice up your markdown notes, for example Zola has [shortcodes](https://www.getzola.org/documentation/content/shortcodes/).

# The resulting design

- Site is generated by Zola. 
- For taking notes from a mobile device I use an open source GitJournal app synced with my site's repository. 
- CI/CD deploys the site for me.