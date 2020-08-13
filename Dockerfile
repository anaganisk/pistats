FROM python:3.6-slim-stretch

# Download required software
RUN apt-get update -y \
    && apt-get -y install \
    i2c-tools \
    sysstat \
    build-essential

ADD ./src /app
COPY requirements.txt /app

WORKDIR /app

ENV TIMEZONE='Asia/Kolkata'

RUN pip install -r requirements.txt

CMD python3 pistat.py
