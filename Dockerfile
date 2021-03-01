
FROM python:3

ENV PYTHONUNBUFFERED = 1

WORKDIR /code

COPY /config/requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

