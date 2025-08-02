---
title: Flying Shooting Game
tags: programming
---

# Scratchpad on a game idea I had recently.

# Core ideas

- You fly around a city in a jetpack-with-wings of sorts
  - Futuristic city, flying cars and stuff
- You have various guns at your disposal
- You are to go from point A to point B, delivering a package
- The attacks you can perform depend on your **speed**
  - The faster you go, the more powerful you are
- You can gain speed:
  - By flying down
  - By using a hook, attaching yourself to vehicles
- The higher you get, the faster cars are flying

# Flying

- Arcade, meant to feel good, not be realistic
- Being able to rapidly turn on dash as an "kind of attack"
- The hook can:
  - Anchor you to neutral entites (cars?)
  - Anchor you to enemies
  - Anchor to buildings (any interesting mechanic there?)
  - You must be careful about relative speeds
  - Hooking way faster objects will damage you
- Cool wings with animations and whatever

## Scenarios

### Deceleration

- Attach some sort of magnet to enemies
- Rapidly decelerate, trading speed for energy
- Get enough energy to fire some cool weapon which would cause all enemies hit with magnets to get pulled together

### Dashing

- Make an enemy which would be fast & deadly
- Make them lock onto the player and stay 10-20m behind
- Instead of shooting, the player should:
  - Fly towards a building
  - Dash last-second
  - The enemies crash into the building

# Music

- I love how Ultrakill synchronizes game with music
- Add pitch-shifting effects when taking damage?
- Music should changed based on the state od the game

# Notes/materials

- https://docs.godotengine.org/en/stable/tutorials/3d/particles/trails.html
- https://docs.godotengine.org/en/stable/tutorials/3d/spring_arm.html
- Godot settings allow for defining blender-style shortcuts, see "begin transformation"
