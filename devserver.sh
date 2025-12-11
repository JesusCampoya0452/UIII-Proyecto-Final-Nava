#!/bin/sh
source .venv/bin/activate
python backend_escuela/manage.py runserver $PORT
