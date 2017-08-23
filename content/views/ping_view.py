import aiohttp_transmute


@aiohttp_transmute.describe(
    paths="/ping"
)
async def ping_get_view(request) -> str:
    "Healthcheck"

    return 'pong'
