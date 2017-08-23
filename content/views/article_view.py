
import aiohttp_transmute

from sqlalchemy.sql.expression import select
from schematics.types import ListType, ModelType


from .helpers import get_record_by_id
from ..serializers import ArticleDetailSerializer
from ..models import Article, User, Comment


JOINT_USER_ARTICLE = Article.join(User, User.c.id == Article.c.user_id)
JOINT_USER_COMMENT = Comment.join(User, User.c.id == Comment.c.user_id)
ARTICLE_SELECT = select([Article, User], use_labels=True).select_from(JOINT_USER_ARTICLE)
COMMENT_SELECT = select([Comment, User], use_labels=True).select_from(JOINT_USER_COMMENT)


@aiohttp_transmute.describe(
    paths="/articles"
)
async def article_get_list_view(request) -> ListType(ModelType(ArticleDetailSerializer)):
    "Get article list"

    async with request.app['db'].acquire() as conn:
        result = await conn.execute(ARTICLE_SELECT)
        articles = await result.fetchall()

        article_ids = [article['article_id'] for article in articles]

        result = await conn.execute(
            COMMENT_SELECT.where(Comment.c.article_id.in_(article_ids))
        )
        comments = await result.fetchall()

        return Article.parse_sql_rows(articles, with_user=True, comments=comments)


@aiohttp_transmute.describe(
    paths="/articles/{article_id}"
)
async def article_get_view(request, article_id: int) -> ArticleDetailSerializer:
    "Get one article"

    async with request.app['db'].acquire() as conn:
        result = await conn.execute(ARTICLE_SELECT.where(Article.c.id == article_id))
        article = await result.fetchone()

        result = await conn.execute(
            COMMENT_SELECT.where(Comment.c.article_id == article_id)
        )
        comments = await result.fetchall()

        return Article.parse_sql_row(article, with_user=True, comments=comments)


@aiohttp_transmute.describe(
    paths="/articles",
    methods="POST"
)
async def article_add_view(request, title: str, text: str, user_id: int) -> ArticleDetailSerializer:
    "Add new article"

    async with request.app['db'].acquire() as conn:
        article_id = await conn.scalar(
            Article.insert().values(
                title=title,
                text=text,
                user_id=user_id,
            )
        )

        return await get_record_by_id(conn, Article, article_id)
