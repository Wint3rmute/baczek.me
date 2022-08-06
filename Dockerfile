FROM fedora:36

RUN dnf install --refresh -y pandoc git graphviz wget
RUN dnf install --refresh -y blas-devel lapack-devel gcc-gfortran g++ poetry gcc
RUN dnf install --refresh -y python39 python-devel cairo-devel
RUN dnf install --refresh -y graphviz

RUN wget -O - "https://github.com/getzola/zola/releases/download/v0.16.0/zola-v0.16.0-x86_64-unknown-linux-gnu.tar.gz" | \
  tar -xvzf - && \
  mv zola /usr/bin/zola && \
  zola --version

WORKDIR /website

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

# Run a test website build
COPY related_posts_generator.py .
COPY content content
COPY static static
COPY templates templates
COPY config.toml .

RUN poetry run python related_posts_generator.py
RUN zola build

# Site autodeploy
COPY site_deploy.sh .
COPY webhook_handler.py .

CMD [ "poetry", "run", "python", "-m", "uvicorn", "webhook_handler:app", "--port", "5555", "--host", "0.0.0.0" ]

