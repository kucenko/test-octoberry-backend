# Octoberry Back-End

## Restrictins

1. python3
1. httpIO
1. pip3

## Install

1. `bash bin/install.sh` - create env via workon
1. `. bin/install_db.sh` - create database

## Run server

Powered by [DevTool](https://github.com/aio-libs/aiohttp-devtools#runserver)

run server: `adev runserver main.py`

## Dockerization

### First build or rebuild

Run command for first builds:

1. create network: `docker network create testoctoberry`
1. build application: `docker-compose up`

Or rebuild:

1. build application: `docker-compose up --build`

### Configuration project

1. run migration (required at first build): `docker-compose run api alembic upgrade head`

### Start docker without build

1. run application: `docker-compose up`

### Where I can find project

Api documentation will be on the page [http://localhost:8000/api/doc](http://localhost:8000/api/doc)
