# [My Personal Website](https://baczek.me)

You should make one for yourself too :)

## Dependencies

1. Install [Zola](https://www.getzola.org/documentation/getting-started/installation/)
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
3. Run `make install`

## Building the site

```bash
make build  # generate assets + zola build
make serve  # zola serve
```

## Other commands

```bash
make check   # run all linters and type checks
make update  # upgrade uv dependencies
```

Show outdated top-level deps:

```bash
uv tree --outdated --depth 1
```
