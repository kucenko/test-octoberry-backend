import sqlalchemy as sa


meta = sa.MetaData()


User = sa.Table(
    'user', meta,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True),
    sa.Column('name', sa.String(200), nullable=False),
)


def parse_sql_row(sql):
    return {
        'id': sql['user_id'],
        'name': sql['user_name'],
    }


def parse_sql_rows(sql):
    return [
        parse_sql_row(row_sql)
        for row_sql in sql
    ]


User.parse_sql_row = parse_sql_row
User.parse_sql_rows = parse_sql_rows
