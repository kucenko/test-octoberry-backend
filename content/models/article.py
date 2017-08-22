import sqlalchemy as sa

from .user import User

meta = sa.MetaData()

Article = sa.Table(
    'article', meta,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('title', sa.String(200), nullable=False),
    sa.Column('text', sa.Text, nullable=False),
    sa.Column('user_id', sa.Integer, sa.ForeignKey(User.c.id), nullable=False),

    # Indexes #
    sa.PrimaryKeyConstraint('id', name='article_id_pkey')
)
