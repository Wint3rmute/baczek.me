FROM archlinux:latest

# python-tomli can be removed when arch fixes poetry packaging
RUN pacman -Sy --noconfirm git graphviz wget \
  blas gcc poetry pkgconf \
  python python-cairo graphviz zola \
  python-tomli \
  && pacman -Sc --noconfirm

WORKDIR /website

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install --only main

# Run a test website build
COPY related_generator related_generator
COPY content content
COPY static static
COPY templates templates
COPY config.toml .

RUN poetry run python -m related_generator
RUN zola build

# Site autodeploy
COPY site_deploy.sh .
COPY webhook_handler.py .

CMD [ "poetry", "run", "python", "-m", "uvicorn", "webhook_handler:app", "--port", "5555", "--host", "0.0.0.0" ]

