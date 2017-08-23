import sqlalchemy as sa

from .helpers import group_by_key
from .user import User
from .comment import Comment

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

meta = sa.MetaData()

Article = sa.Table(
    'article', meta,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True),
    sa.Column('title', sa.String(200), nullable=False),
    sa.Column('text', sa.Text, nullable=False),
    sa.Column('user_id', sa.Integer, sa.ForeignKey(User.c.id), nullable=False),
)


def parse_sql_row(sql, with_user=False, comments=None):
    article = {
        'id': sql['article_id'],
        'title': sql['article_title'],
        'text': sql['article_text'],
    }

    if with_user:
        article['user'] = User.parse_sql_row(sql)

    if comments:
        article['comments'] = Comment.parse_sql_rows(comments, with_user=with_user)

    return article


def parse_sql_rows(sql, comments, **kwargs):
    dict_comments = group_by_key(comments, 'comment_article_id')

    return [
        parse_sql_row(
            row_sql,
            with_user=True,
            comments=dict_comments.get(row_sql['article_id'], None)
        )
        for row_sql in sql
    ]


Article.parse_sql_row = parse_sql_row
Article.parse_sql_rows = parse_sql_rows
