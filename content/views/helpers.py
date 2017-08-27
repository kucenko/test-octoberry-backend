import math

from aiohttp.web import HTTPNotFound
from sqlalchemy import func


async def get_record_by_id(conn, type_record, record_id):
    result = await conn.execute(
        type_record.select().where(type_record.c.id == record_id)
    )

    return await result.fetchone()


async def get_paginated_records(conn, query, page, model):
    count_query = query.with_only_columns([func.count(model.c.id)]).order_by(None)
    count_recors = await conn.scalar(count_query)
    total_pages = math.ceil(float(count_recors)/10)

    pagination = {
        'total_pages': total_pages
    }

    records = await conn.execute(
        query.offset((page - 1) * 10).limit(10)
    )

    return {
        "data": records,
        "pagination": pagination
    }


async def fetch_one_or_404(model):
    res = await model.fetchone()

    if not res:
        raise HTTPNotFound()

    return res
