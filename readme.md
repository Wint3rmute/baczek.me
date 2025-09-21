# [My Personal Website](https://baczek.me)

You should make one for yourself too :)

## Building

I'm using [Zola](https://www.getzola.org/) + some extra scripts to build my
[site map and related pages](https://baczek.me/map).

If you have [Poetry](https://python-poetry.org/) and [Zola](https://www.getzola.org/) installed, simply run:

```bash
poetry install
poetry run python -m exocortex
zola serve  # for development
# or
zola build  # for production
```

You can also use the convenient build script: `./scripts/build.sh`

Refer to the [CI build job definition](./.github/workflows/build.yml) for details on the complete build process.
