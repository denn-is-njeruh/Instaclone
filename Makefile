SHELL := /bin/bash

include .env

install:
	pipenv install

serve:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser
