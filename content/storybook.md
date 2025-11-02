---
title: Storybook
tags: meta
---

This page displays all the building blocks of the site. I use it for visual
inspection when changing the [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS).

# H1 Header

## H2 Header

### H3 Header

#### H4 Header

Horizontal bar:

---

> Here we have a quote by someone great!
>
> ~ Someone Great

Text samples! Here's *some italic*. Now, it's **time to be bold!**. `The Race
For Monospace`. ~~You can't see me!~~.

```c
float Q_rsqrt( float number )
{
  long i;
  float x2, y;
  const float threehalfs = 1.5F;
  
  x2 = number * 0.5F;
  y  = number;
  i  = * ( long * ) &y;                       // evil floating point bit level hacking
  i  = 0x5f3759df - ( i >> 1 );               // what the fuck?
  y  = * ( float * ) &i;
  y  = y * ( threehalfs - ( x2 * y * y ) );   // 1st iteration
  //	y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed
  
  return y;
}
```

At last, [an external link](https://detondev.com). Alternatively [an internal
link](/now).

