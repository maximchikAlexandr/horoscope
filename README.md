
# Horoscope
## About project

Project **Horoscope** is a web application designed to help users receive personalized horoscopes 
every day. This project written in Python using the *Django* framework.

For installation using the *Docker*, the project contains two containers: the Django application 
and the *PostgreSQL* database.


## Installation

Clone the repository from GitHub:

```sh
git clone https://github.com/maximchikAlexandr/horoscope.git
```

Create a file named '.env' in the root directory:

```sh
cd horoscope/
nano .env
```

and fill it with the following environment variables:

```sh
# Django parameters
DEBUG=True
DJANGO_SECRET_KEY="the_key_used_for_encryption"

# database parameters
DB_ENGINE="django.db.backends.postgresql_psycopg2"
POSTGRES_DB="database_name" 
POSTGRES_USER="your_database_username"
POSTGRES_PASSWORD="your_database_password"
DB_HOST="your_database_host"
DB_PORT="port_of_your_database_in_container"
DB_OUT_PORT="outer_port_of_your_database"
```

Create and start the docker containers:

```sh
docker compose up -d
```

Open up the browser and navigate to the main page of the project at http://localhost:8000/.