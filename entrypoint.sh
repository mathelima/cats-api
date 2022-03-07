#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn cats_api.wsgi -b 0.0.0.0:8000