FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN git clone https://github.com/mitsest/paging_api.git
COPY . /code/
RUN ls
RUN pip install -r Requirements
