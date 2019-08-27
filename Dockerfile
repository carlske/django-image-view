FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv 
RUN mkdir /imageView
WORKDIR /imageView
COPY requirements.txt /imageView/

RUN pipenv install
COPY . /imageView/