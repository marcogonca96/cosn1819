FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN python manage.py makemigrations catalogue
RUN python manage.py migrate
RUN python manage.py loaddata catalogue_trailerflix/fixtures/category_fixtures.json
RUN python manage.py loaddata catalogue_trailerflix/fixtures/catalogue_fixtures.json
CMD [ "python", "manage.py runserver 0.0.0.0:8000" ]