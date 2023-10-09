# Personal Website

You should make one for yourself too :)

## Building

I'm using [Zola](https://www.getzola.org/) + some extra scripts to build my
[site map and related pages](https://baczek.me/map).

If you have [Poetry](https://python-poetry.org/) installed, simply run `poetry
install` and `poetry run ipython exocortex.ipynb` and then `zola serve` or
`zola build`.

If you prefer to keep everything isolated, use the [`Dockerfile`](./Dockerfile)
to build an image which can then run the commands above. Refer to the [CI build
job definition](./.github/workflows/zola.yml) for details.
