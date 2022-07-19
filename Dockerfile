FROM archlinux:latest

RUN pacman -Sy --noconfirm
RUN pacman -S zola pandoc git python-scikit-learn python-scipy python-graphviz --noconfirm
RUN zola --version

COPY docker_deploy.sh .

CMD [ "./docker_deploy.sh" ]

