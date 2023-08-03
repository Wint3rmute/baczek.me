FROM archlinux:latest as builder
RUN pacman -Syu --noconfirm git graphviz wget \
  blas gcc poetry pkgconf \
  python python-cairo graphviz zola \
  && pacman -Sc --noconfirm

WORKDIR /website
COPY pyproject.toml poetry.lock poetry.toml /website/
RUN poetry install --only main && rm -rf ~/.cache/pypoetry

FROM archlinux:latest
RUN pacman -Sy --noconfirm git graphviz wget \
  blas \
  python python-cairo graphviz zola \
  && pacman -Sc --noconfirm

COPY --from=builder /website /website
