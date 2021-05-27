release: python  project/manage.py migrate
web: gunicorn --pythonpath project config.wsgi --log-file -