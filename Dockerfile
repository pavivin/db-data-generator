FROM python:3.10.6-slim-buster


RUN apt-get update && \
    apt-get install -y curl \
    wget \
    openjdk-8-jdk
RUN mkdir -p usr/app
WORKDIR /usr/app

ADD . /usr/app/
RUN mkdir -p usr/app/src/data

RUN pip install -U pip && pip install -r requirements.min.txt

ENV PYTHONPATH=/app/src

EXPOSE 8001
WORKDIR /usr/app/src

CMD ["python", "main.py"]
