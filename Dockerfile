FROM fedora:36

# Related posts generation
#RUN pacman -Sy zola pandoc git gcc gcc-fortran poetry cblas lapack --noconfirm

RUN dnf install --refresh -y pandoc zola git gcc poetry
RUN dnf install --refresh -y blas-devel lapack-devel

WORKDIR /website

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

# Run a test website build
COPY related_posts_generator.py .
COPY content .
COPY static .
COPY templates .
COPY config.toml .

RUN poetry run python related_posts_generator.py
RUN zola build


# Auto-deploy
RUN pacman -S python-fastapi uvicorn --noconfirm

COPY site_deploy.sh .
COPY webhook_handler.py .

CMD [ "uvicorn", "webhook_handler:app", "--port", "5555", "--host", "0.0.0.0" ]

