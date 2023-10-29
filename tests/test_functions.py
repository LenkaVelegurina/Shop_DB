import pandas as pd
import os
import psycopg2 as pg
import unittest
from dataclasses import dataclass


@dataclass
class Credentials:
    dbname: str = "pg_db"
    host: str = "127.0.0.1"
    port: int = 5432
    user: str = "postgres"
    password: str = "postgres"


def psycopg2_conn_string():
    return f"""
        dbname='{os.getenv("DBNAME", Credentials.dbname)}' 
        user='{os.getenv("DBUSER", Credentials.user)}' 
        host='{os.getenv("DBHOST", Credentials.host)}' 
        port='{os.getenv("DBPORT", Credentials.port)}' 
        password='{os.getenv("DBPASSWORD", Credentials.password)}'
 """


def set_connection():
    return pg.connect(psycopg2_conn_string())


class TestHardQueries(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHardQueries, self).__init__(*args, **kwargs)
        self.conn = set_connection()
        self.cursor = self.conn.cursor()

    def test1(self):
        query = """
            SELECT *
            FROM shop.get_carpet_info(1);
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 9
        assert result.shape[0] == 1
        assert result.iloc[0].loc['carpet_id'] >= 1
        assert result.iloc[0].loc['length'] >= 1
        assert result.iloc[0].loc['width'] >= 1
        assert result.iloc[0].loc['price'] >= 1
        assert result.iloc[0].loc['amount'] >= 0

    def test2(self):
        query = """
            SELECT *
            FROM shop.get_total_carpet_amount();
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 1
        assert result.shape[0] == 1
        assert result.iloc[0].loc['get_total_carpet_amount'] >= 0

    def end(self):
        self.cursor.close()
        self.conn.close()
