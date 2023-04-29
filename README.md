# Horoscope

## Installation

Install the dependencies and devDependencies and start the server.

Clone the repository from GitHub:

```sh
git clone https://github.com/maximchikAlexandr/horoscope.git
```

Create a file .env in the root directory:

```sh
cd horoscope/
nano .env
```

and fill the following environment variables:

```sh
DB_ENGINE='django.db.backends.postgresql_psycopg2'
POSTGRES_DB=some_database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=some_password
DB_HOST=localhost
DB_PORT=some_port_in_container
DB_OUT_PORT=some_port_out_container
DEBUG=True
DJANGO_SECRET_KEY=some_secret_key
```

Create and start the docker containers:

```sh
docker compose up -d
```