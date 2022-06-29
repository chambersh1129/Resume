FROM python:3.10-alpine

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIER /code

copy ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
