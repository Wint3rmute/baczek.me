# [My Personal Website](https://baczek.me)

You should make one for yourself too :)

## Dependencies

1. Install [Zola](https://www.getzola.org/documentation/getting-started/installation/)
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
3. Run `uv sync`

## Building the site

```bash
uv run exocortex
zola serve # or `zola build`
```

> [!NOTE]
> Alternatively, refer to the [CI build job definition](./.github/workflows/build.yml).

## Notes

Show outdated top-level deps:

```bash
uv tree --outdated --depth 1
```
