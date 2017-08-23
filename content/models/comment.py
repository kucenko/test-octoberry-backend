import sqlalchemy as sa

from .user import User
# from .article import Article

meta = sa.MetaData()

Comment = sa.Table(
    'comment', meta,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True),
    sa.Column('text', sa.String(200), nullable=False),
    sa.Column('user_id', sa.Integer, sa.ForeignKey(User.c.id), nullable=False),
    sa.Column('article_id', sa.Integer, sa.ForeignKey('article.id'), nullable=False),  # Article.c.id for alembic
)


def parse_sql_row(sql, with_user=False):
    comment = {
        'id': sql['comment_id'],
        'text': sql['comment_text'],
    }

    if with_user:
        comment['user'] = User.parse_sql_row(sql)

    return comment


def parse_sql_rows(sql, **kwargs):
    return [
        parse_sql_row(
            row_sql,
            **kwargs
        )
        for row_sql in sql
    ]


Comment.parse_sql_row = parse_sql_row
Comment.parse_sql_rows = parse_sql_rows
