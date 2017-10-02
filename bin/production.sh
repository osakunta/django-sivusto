#!/bin/bash

echo "Make database migrations"
python manage.py makemigrations

echo "Apply database migrations"
python manage.py migrate

echo "Collect static files to one location"
python manage.py collectstatic

echo "Starting Gunicorn"
exec gunicorn sato.wsgi:application \
    --bind 0.0.0.0:8010 \
    --workers 3 \
    -t 120
