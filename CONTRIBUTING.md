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

#### Install NLTK data

```shell
python -m nltk.downloader all
```

#### Migrate the database

```shell
./manage.py migrate
```

#### Load CanLII seed data

```shell
./load_canlii_documents.sh
```

#### Start Django

```shell
./manage.py runserver
```

#### Start worker

```shell
celery -A baker_street worker -l info
```

## Deploying

We're using [Dokku Alternative][dokku-alt] on Amazon Web Services. First contact @elliottsj to add your public
key to the server, then add the remote and push to deploy:

```shell
git remote add dokku dokku@sherlocke.me:sherlocke.me
git push dokku
```

[dokku]:     https://github.com/progrium/dokku
[dokku-alt]: https://github.com/dokku-alt/dokku-alt
