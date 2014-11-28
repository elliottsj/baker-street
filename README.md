baker-street
============

Web service for Sherlocke to talk to Watson

## Overview

*baker-street* powers Sherlocke, allowing it to communicate with IBM Watson and CanLII.
It handles user accounts and billing for Sherlocke users, and keeps track of which documents and questions
have been accessed by each user.

## Setup

To setup first initialize the database, this may take a while.

`python ./manage.py syncdb`

then initialize the background process:

`celery -A baker_street worker -l info`

1st-party libraries in use:
- [pycanlii](https://github.com/sherlocke/pycanlii)
- [pywatson](https://github.com/sherlocke/pywatson)

3rd-party libraries in use:

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](http://www.django-rest-framework.org/)
- [Django Suit](http://djangosuit.com/)



