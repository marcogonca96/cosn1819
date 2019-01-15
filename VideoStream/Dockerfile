FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev
RUN mkdir /code

WORKDIR /code

ADD ./requirements.txt /code/

RUN pip install -r requirements.txt

RUN export FLASK_APP=main.py
RUN export FLASK_ENV=development

ADD . /code/

CMD ["python", "main.py"]
