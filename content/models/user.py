import sqlalchemy as sa

meta = sa.MetaData()

User = sa.Table(
    'user', meta,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('name', sa.String(200), nullable=False),

    # Indexes #
    sa.PrimaryKeyConstraint('id', name='user_id_pkey')
)
