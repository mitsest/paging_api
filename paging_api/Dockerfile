FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY Requirements /code/
RUN pip install -r Requirements
COPY . /code/
