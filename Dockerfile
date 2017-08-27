FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
# RUN chmod +x main.py
RUN pip install -r requirements/prod.txt