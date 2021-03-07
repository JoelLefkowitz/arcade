from inspect import cleandoc

import aiopg
from safe_environ import from_env

from .models import Score


async def insert_score(score):
    async with aiopg.create_pool(
        data_source()
    ) as pool, pool.acquire() as conn, conn.cursor() as cur:
        await cur.execute(
            cleandoc(
                """
                INSERT INTO scores_score (Name, Value)
                VALUES (%s, %s);
                """
            ),
            (score.name, score.value),
        )


async def get_top_scores(count=5):
    async with aiopg.create_pool(
        data_source()
    ) as pool, pool.acquire() as conn, conn.cursor() as cur:
        await cur.execute(
            cleandoc(
                """
                SELECT Name, Value
                FROM scores_score 
                ORDER BY Value 
                DESC LIMIT %s;
                """
            ),
            (count,),
        )

        return [Score(*i) async for i in cur]


def data_source(
    host=from_env("POSTGRES_HOST"),
    dbname=from_env("POSTGRES_DB"),
    user=from_env("POSTGRES_USER"),
    password=from_env("POSTGRES_PASSWORD"),
    port=5432,
):
    return " ".join(
        [
            f"dbname={dbname}",
            f"user={user}",
            f"password={password}",
            f"host={host}",
            f"port={port}",
        ]
    )
