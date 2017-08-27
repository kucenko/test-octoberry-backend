# Octoberry Back-End

## Restrictins

1. python3
1. httpIO
1. pip3

## Install

1. `bash bin/install.sh` - create env via workon
1. `. bin/install_db.sh` - create database

## Run server

[DevTool](https://github.com/aio-libs/aiohttp-devtools#runserver)

run server: `adev runserver main.py`

## Dockerization

1. `docker-compose run web` - Install project at first
1. `docker-compose up` - rerun application

### New site

To fin api go to the [site](http://localhost:8001/api/doc)

### Install db

Run shell from `db` container and run commands from '`bin/install_db.sh`

### Migration

Run shell from `web-api` and migration all from alembic
