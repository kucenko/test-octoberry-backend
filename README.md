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

1. create network: `docker network create testoctoberry`
1. `docker-compose up` - rerun application
1. open console for db and run commands from `bit/install_db.sh` for create a new db
1. open consolse for `test-octoberry-api` and run `alembic upgrade head` to migrate

### new version

1. create network: `docker network create testoctoberry`
1. `docker-compose build` - build application
1. `docker-compose run api alembic upgrade head` run migration

### New site

To fin api go to the [site](http://localhost:8001/api/doc)

### Install db

Run shell from `db` container and run commands from '`bin/install_db.sh`

### Migration

Run shell from `web-api` and run migration: `alembic upgrade head`
