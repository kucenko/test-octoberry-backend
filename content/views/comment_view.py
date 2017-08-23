
import aiohttp_transmute

from sqlalchemy.sql.expression import select
from schematics.types import ListType, ModelType


from .helpers import get_record_by_id
from ..serializers import CommentSerializer
from ..models import User, Comment


JOINT_USER_COMMENT = Comment.join(User, User.c.id == Comment.c.user_id)
COMMENT_SELECT = select([Comment, User], use_labels=True).select_from(JOINT_USER_COMMENT)


@aiohttp_transmute.describe(
    paths="/comments"
)
async def comment_get_list_view(request, user_id: int=None) -> ListType(ModelType(CommentSerializer)):
    "Get list of comments"

    async with request.app['db'].acquire() as conn:
        query = COMMENT_SELECT

        if user_id:
            query = query.where(User.c.id == user_id)

        comments = await conn.execute(query)

        return Comment.parse_sql_rows(comments, with_user=True)


@aiohttp_transmute.describe(
    paths="/comments",
    methods="POST"
)
async def comment_add_view(request, text: str, user_id: int, article_id: int) -> CommentSerializer:
    "Add new comment"

    async with request.app['db'].acquire() as conn:
        comment_id = await conn.scalar(
            Comment.insert().values(
                text=text,
                user_id=user_id,
                article_id=article_id,
            )
        )

        return await get_record_by_id(conn, Comment, comment_id)


@aiohttp_transmute.describe(
    paths="/comments/{comment_id}",
    methods="POST"
)
async def comment_edit_view(request, text: str, comment_id: int) -> CommentSerializer:
    "Edit comment"

    async with request.app['db'].acquire() as conn:
        await conn.execute(
            Comment.update().values(text=text).where(User.c.id == comment_id)
        )

        return await get_record_by_id(conn, Comment, comment_id)
