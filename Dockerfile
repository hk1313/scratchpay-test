# pull the official docker image
FROM python:3.9.4-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    gcc \
    wget

RUN pip install setuptools==65.6.3

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .