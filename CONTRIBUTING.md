## Development

To set up your development environment:

#### Install Python

- [pyenv](https://github.com/yyuu/pyenv) recommended.

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

#### Create the database and set `DATABASE_URL`

```shell
psql --command="CREATE DATABASE baker_street_development;"
export DATABASE_URL="postgresql://localhost/baker_street_development"
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

#### Create an OAuth application for the Chrome Extension

- Open <http://localhost:8000/o/applications/register>
- Fill out the form:
  - Name: `sherlocke-chrome-dev`
  - Client id: `sherlocke-chrome-dev`
  - Client secret: (leave default)
  - Client type: Confidential
  - Authorization grant type: Implicit
  - Redirect uris: `https://<extension-id>.chromiumapp.org/provider_cb`
    where `<extension-id>` is the Sherlocke extension ID from <chrome://extensions/>

## Deploying

We're using [Dokku Alternative][dokku-alt] on Amazon Web Services. First contact @elliottsj to add your public
key to the server, then add the remote and push to deploy:

```shell
git remote add dokku dokku@sherlocke.me:sherlocke.me
git push dokku
```

To proxy requests from *http://sherlocke.me* to *http://baker-street.sherlocke.me*, 
add `/etc/nginx/conf.d/www.conf`:

```
server {
  server_name sherlocke.me;

  location / {
    proxy_pass http://baker-street.sherlocke.me;
  }
}
```

[dokku]:     https://github.com/progrium/dokku
[dokku-alt]: https://github.com/dokku-alt/dokku-alt
