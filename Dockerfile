FROM archlinux:latest as builder

# python-tomli can be removed when arch fixes poetry packaging
RUN pacman -Sy --noconfirm git graphviz wget \
  blas gcc poetry pkgconf \
  python python-cairo graphviz zola \
  python-tomli \
  && pacman -Sc --noconfirm

WORKDIR /website

COPY pyproject.toml poetry.lock poetry.toml /website/

RUN poetry install --only main

# Run a test website build
COPY related_generator related_generator
COPY content content
COPY static static
COPY templates templates
COPY config.toml .

RUN poetry run python -m related_generator
RUN zola build
RUN du -sh /website

FROM archlinux:latest

COPY --from=builder /website /
COPY --from=builder /root/nltk_data /root

# Site autodeploy
COPY site_deploy.sh .
COPY webhook_handler.py .

RUN pacman -Sy --noconfirm git graphviz wget \
  blas poetry \
  python python-cairo graphviz zola \
  python-tomli \
  && pacman -Sc --noconfirm

CMD [ "poetry", "run", "python", "-m", "uvicorn", "webhook_handler:app", "--port", "5555", "--host", "0.0.0.0" ]

