# module db.py in your program
from psycopg_pool import ConnectionPool
from dotenv import dotenv_values

pool = ConnectionPool(dotenv_values(".env")['PG_CONNECTION'])
# the pool starts connecting immediately.


def query(query: str, args: list = []):
    with pool.connection() as conn:
        return conn.execute(query, args).fetchall()
