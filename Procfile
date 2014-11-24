web: gunicorn baker_street.wsgi --log-file -
worker: celery -A baker_street worker -l info
