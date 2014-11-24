web: gunicorn baker_street.wsgi --log-file -
worker: celery worker --app=baker_street --loglevel=info
