FROM archlinux:latest

RUN pacman -Sy --noconfirm
RUN pacman -S zola git python-scikit-learn python-scipy graphwiz --noconfirm
RUN zola --version

COPY docker_deploy.sh .

CMD [ "./docker_deploy.sh" ]

