import aiohttp_transmute

from sqlalchemy.sql.expression import select
from schematics.types import ModelType, ListType

from .helpers import get_record_by_id
from ..serializers import UserSerializer
from ..models import User


@aiohttp_transmute.describe(
    paths="/users",
)
async def user_get_list_view(request) -> ListType(ModelType(UserSerializer)):
    """
    Get all users. Development
    """

    async with request.app['db'].acquire() as conn:
        result = await conn.execute(select([User], use_labels=True))
        users = await result.fetchall()

        return User.parse_sql_rows(users)

@aiohttp_transmute.describe(
    paths="/users",
    methods="POST"
)
async def user_add_view(request, name: str) -> UserSerializer:
    """
    Add new user
    """

    async with request.app['db'].acquire() as conn:
        user_id = await conn.scalar(
            User.insert().values(name=name)
        )

        return await get_record_by_id(conn, User, user_id)


@aiohttp_transmute.describe(
    paths="/users/{user_id}",
    methods="PUT"
)
async def user_edit_view(request, name: str, user_id: int) -> UserSerializer:
    """
    Edit user
    """

    async with request.app['db'].acquire() as conn:
        await conn.execute(
            User.update().values(name=name).where(User.c.id == user_id)
        )

        return await get_record_by_id(conn, User, user_id)
