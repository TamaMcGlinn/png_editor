FROM debian:latest
COPY src/ /opt/application
WORKDIR /opt/application
