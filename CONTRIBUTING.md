## Development

To set up your development environment:

#### Install PostgreSQL

[Installation varies by platform](http://www.postgresql.org/download/).

Once installed, the `pg_config` executable must be on your `PATH`.
Setup varies by platform; [here are instructions for Postgres.app](http://postgresapp.com/documentation/cli-tools.html)

#### Use virtualenv

```shell
cd baker-street/
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

#### Install dependencies

```shell
pip install -r requirements.txt
bundle install
```

#### Migrate the database

```shell
./manage.py migrate
```

#### Start Django

```shell
./manage.py runserver
```
