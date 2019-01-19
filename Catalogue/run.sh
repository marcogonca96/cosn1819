#!/bin/sh
python manage.py makemigrations catalogue
python manage.py migrate
python manage.py loaddata catalogue_trailerflix/fixtures/category_fixtures.json
python manage.py loaddata catalogue_trailerflix/fixtures/catalogue_fixtures.json
python manage.py runserver 0.0.0.0:8000