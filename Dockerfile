FROM archlinux:latest as builder
RUN pacman -Sy --noconfirm git graphviz wget \
  blas gcc poetry pkgconf \
  python python-cairo graphviz zola \
  && pacman -Sc --noconfirm

WORKDIR /website
COPY pyproject.toml poetry.lock poetry.toml /website/
RUN poetry install --only main && rm -rf ~/.cache/pypoetry

# Run a test website build
COPY related_generator related_generator
COPY content content
COPY static static
COPY templates templates
COPY config.toml .

RUN poetry run python -m related_generator && zola build && du -sh /website/public && rm -rf /website/public

FROM archlinux:latest
RUN pacman -Sy --noconfirm git graphviz wget \
  blas poetry \
  python python-cairo graphviz zola \
  && pacman -Sc --noconfirm

COPY --from=builder /website /
COPY site_deploy.sh .
COPY webhook_handler.py .

CMD [ "poetry", "run", "python", "-m", "uvicorn", "webhook_handler:app", "--port", "5555", "--host", "0.0.0.0" ]

