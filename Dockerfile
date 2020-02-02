FROM python:latest
MAINTAINER Lidor
ARG devops=docker

RUN apt-get update  && \
    apt-get upgrade -y && \
    apt-get install vim nano curl wget && \
    mkdir /app && \
    echo ${devops}

WORKDIR /app
COPY . .
EXPOSE 80
ENV BUILD_ID=11
ENV ENVIRONMENT=QA
CMD [ "python3", "programflow.py"]


