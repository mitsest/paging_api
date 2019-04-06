FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN git clone https://github.com/mitsest/paging_api.git
COPY . /code/
RUN pip install -r Requirements

