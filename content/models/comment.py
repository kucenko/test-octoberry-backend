import sqlalchemy as sa

meta = sa.MetaData()

Comment = sa.Table(
    'comment', meta,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('text', sa.String(200), nullable=False),
    sa.Column('user_id', sa.Integer, sa.ForeignKey("user.user_id"), nullable=False),

    # Indexes #
    sa.PrimaryKeyConstraint('id', name='question_id_pkey')
)