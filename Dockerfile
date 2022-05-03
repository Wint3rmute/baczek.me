FROM archlinux:latest

RUN pacman -Sy --noconfirm
RUN pacman -S zola git --noconfirm
RUN zola --version

COPY docker_deploy.sh .

CMD [ "./docker_deploy.sh" ]

