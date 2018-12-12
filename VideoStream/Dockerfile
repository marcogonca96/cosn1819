FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /trailix/requirements.txt

WORKDIR /trailix

RUN pip install -r requirements.txt

RUN export FLASK_APP=main.py
RUN export FLASK_ENV=development

COPY . /trailix

#ENTRYPOINT [ "python" ]
CMD ["python", "main.py"]
