@echo off

rem Install project dependencies using pip
pip install -r requirements.txt

rem Collect static files
python manage.py collectstatic --no-input

rem Run database migrations
python manage.py migrate

