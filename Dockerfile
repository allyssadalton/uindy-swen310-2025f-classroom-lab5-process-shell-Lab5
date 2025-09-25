FROM ubuntu:22.04

ARG DEBIAN_FRONTEND="noninteractive"

RUN mkdir -p /home/app
WORKDIR /home/app

# replace bourne with bash to be able to source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh


# update the repository sources list and install dependencies
# apt-get install -y curl wget
RUN apt-get update \
    && apt-get install -y \
    curl \
    wget \
    ca-certificates \
    sudo \
    libx11-6 \
    vim \
    nano \
    software-properties-common \
    gcc \
    && apt-get -y autoclean
    

EXPOSE 8888

CMD [ "/bin/bash" ]
