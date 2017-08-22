#!/usr/bin/env python
import aiohttp_transmute

from aiohttp import web

from content.router import setup_routes


app = web.Application()

setup_routes(app)
aiohttp_transmute.add_swagger(app, '/api/doc.json', '/api/doc')

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8000)
