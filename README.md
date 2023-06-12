#Django Bootstrap Free Admin Theme

py -3 -m venv venv
venv\Scripts\activate
pip install -r req
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
*enjoy*