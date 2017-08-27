import yaml
import os

from aiopg.sa import create_engine


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'base.yml'), 'r') as ymlfile:
    config = yaml.load(ymlfile)


async def init_pg(app):
    db_config = config['postgres']

    engine = await create_engine(
        database=os.getenv('DATABASE_NAME', db_config['database']),
        user=os.getenv('DATABASE_USERNAME', db_config['user']),
        password=os.getenv('DATABASE_PASSWORD', db_config['password']),
        host=os.getenv('DATABASE_HOST', db_config['host']),
        port=os.getenv('DATABASE_PORT', db_config['port']),
        minsize=db_config['minsize'],
        maxsize=db_config['maxsize']
    )

    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
