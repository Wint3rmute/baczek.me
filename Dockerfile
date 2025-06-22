FROM archlinux:latest AS builder
RUN pacman -Syu --noconfirm git graphviz wget \
  blas gcc poetry pkgconf \
  python python-cairo graphviz zola \
  && pacman -Sc --noconfirm

WORKDIR /build
COPY pyproject.toml poetry.lock poetry.toml /build/
RUN poetry install --only main --no-root && rm -rf ~/.cache/pypoetry

FROM archlinux:latest
RUN pacman -Syu --noconfirm git graphviz wget \
  blas \
  poetry python python-cairo graphviz zola \
  && pacman -Sc --noconfirm

COPY --from=builder /build /build
