FROM archlinux:latest AS builder
RUN pacman -Syu --noconfirm git graphviz wget \
  blas gcc pkgconf \
  python python-cairo graphviz zola python-pip \
  && pacman -Sc --noconfirm

RUN pip install --break-system-packages uv

WORKDIR /build
COPY pyproject.toml uv.lock /build/
RUN uv sync && rm -rf ~/.cache/uv

FROM archlinux:latest
RUN pacman -Syu --noconfirm git graphviz wget \
  blas \
  python python-cairo graphviz zola python-pip \
  && pacman -Sc --noconfirm

RUN pip install --break-system-packages uv

COPY --from=builder /build /build
