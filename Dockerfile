FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /quizapp

RUN pip install -r requirements.txt
