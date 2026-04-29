# [My Personal Website](https://baczek.me)

You should make one for yourself too :)

## Dependencies

1. Install [Zola](https://www.getzola.org/documentation/getting-started/installation/)
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Quickstart

```bash
make install  # install dependencies
make          # build the site and serve it locally
```

## All commands

| Command | Description |
|---|---|
| `make install` | Install dependencies |
| `make` | Build the site and serve it locally |
| `make build` | Generate assets + run `zola build` |
| `make serve` | Run `zola serve` |
| `make check` | Run all linters and type checks |
| `make update` | Upgrade uv dependencies |

Show outdated top-level deps:

```bash
uv tree --outdated --depth 1
```
