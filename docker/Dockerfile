FROM python:3.10.5
MAINTAINER Asher

WORKDIR /app

RUN apt-get update && apt-get install --no-install-recommends -y \
  nano \
  vim-tiny \
  binutils \
  libproj-dev \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD university_panel /app/university_panel

ENV PYTHONUNBUFFERED 1

WORKDIR /app/university_panel/

