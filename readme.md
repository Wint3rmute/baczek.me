# [My Personal Website](https://baczek.me)

You should make one for yourself too :)

## Dependencies

1. Install [Zola](https://www.getzola.org/documentation/getting-started/installation/)
2. Install [Poetry](https://python-poetry.org/)
3. Run `poetry install`

## Building the site

```bash
poetry run python -m exocortex
zola serve # or `zola build`
```

> [!NOTE]
> Alternatively, refer to the [CI build job definition](./.github/workflows/build.yml).

## Notes

Show outdated top-level deps:

```bash
poetry show -To
```
