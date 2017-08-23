import aiohttp_transmute

from aiohttp import web

from config.base import init_pg, close_pg

from .views import route_views


content_api_app = web.Application()


content_api_app.on_startup.append(init_pg)
content_api_app.on_cleanup.append(close_pg)


def setup_routes(app):
    for view in route_views:
        aiohttp_transmute.route(content_api_app, view)

    content_api_app.router.add_get(
        '/doc/swagger.json',
        aiohttp_transmute.create_swagger_json_handler(content_api_app, base_path='/api')
    )
    aiohttp_transmute.add_swagger_api_route(content_api_app, '/doc', '/api/doc/swagger.json')

    app.add_subapp('/api', content_api_app)
