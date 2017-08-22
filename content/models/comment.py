import sqlalchemy as sa

from .user import User

meta = sa.MetaData()

Comment = sa.Table(
    'comment', meta,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('text', sa.String(200), nullable=False),
    sa.Column('user_id', sa.Integer, sa.ForeignKey(User.c.id), nullable=False),

    # Indexes #
    sa.PrimaryKeyConstraint('id', name='comment_id_pkey')
)
