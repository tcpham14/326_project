#! /bin/bash

# A script that automates the reconstruction of the entire database.
rm -f db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py shell < init.py
