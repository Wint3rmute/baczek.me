FROM archlinux:latest

RUN pacman -Sy --noconfirm
# Related posts generation
RUN pacman -S zola pandoc git python-scikit-learn python-scipy python-graphviz --noconfirm
# Auto-deploy
RUN pacman -S python-fastapi uvicorn --noconfirm

COPY site_deploy.sh .
COPY webhook_handler.py .

CMD [ "uvicorn", "webhook_handler:app", "--port", "5555", "--host", "0.0.0.0" ]

