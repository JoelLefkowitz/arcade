import asyncio
from safe_environ import from_env
import aiopg


async def insert_score():
    async with aiopg.create_pool(dsn()) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute()


def dsn(
    dbname=from_env("POSTGRES_DB"),
    user=from_env("POSTGRES_USER"),
    password=from_env("POSTGRES_PASSWORD"),
    host="127.0.0.1",
):
    return f"dbname={dbname} user={user} password={password} host={host}"
