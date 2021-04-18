#!/bin/sh

export DJANGO_SETTINGS_MODULE="arcade_server.settings.prod"
python manage.py migrate

echo "Gunicorn binding to :8000"
gunicorn arcade_server.wsgi -b :8000
