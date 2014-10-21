baker-street
============

Web service for Sherlocke to talk to Watson

## Overview

*baker-street* powers Sherlocke, allowing it to communicate with IBM Watson and CanLII.
It handles user accounts and billing for Sherlocke users, and keeps track of which documents and questions
have been accessed by each user.

3rd-party libraries in use:

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](http://www.django-rest-framework.org/)
- [Django Suit](http://djangosuit.com/)
- [pycanlii](https://github.com/sherlocke/pycanlii)
- [pywatson]()

## Development

To set up your development environment:

#### Install PostgreSQL

[Installation varies by platform](http://www.postgresql.org/download/)

Once installed, the `pg_config` executable must be on your `PATH`.
Setup varies by platform; [here are instructions for Postgres.app](http://postgresapp.com/documentation/cli-tools.html)

#### (Optional) Use virtualenv

```shell
cd baker-street/
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

#### Install dependencies

```shell
pip install -r requirements.txt
```

#### Migrate the database

```shell
./manage.py migrate
```

#### Start Django

```shell
./manage.py runserver
```
