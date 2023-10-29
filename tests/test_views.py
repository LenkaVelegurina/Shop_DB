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
            FROM shop.supply_view;
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 4
        for i in range(result.shape[0]):
            assert '*******' in result.iloc[i].loc['address']
        assert result.iloc[0].loc['date_from'] <= \
               result.iloc[0].loc['date_to']
        for i in range(1, result.shape[0]):
            assert result.iloc[i].loc['date_from'] >= \
                   result.iloc[i - 1].loc['date_from']
            assert result.iloc[i].loc['date_from'] <= \
                   result.iloc[i].loc['date_to']

    def test2(self):
        query = """
            SELECT *
            FROM shop.carpet_info_view;
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 3
        for i in range(1, result.shape[0]):
            assert result.iloc[i].loc['price'] >= \
                   result.iloc[i - 1].loc['price']

    def test3(self):
        query = """
            SELECT *
            FROM shop.carpet_sales_by_producer;
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 3
        for i in range(1, result.shape[0]):
            assert result.iloc[i].loc['total_sales'] <= \
                   result.iloc[i - 1].loc['total_sales']

    def test4(self):
        query = """
            SELECT *
            FROM shop.average_price_by_producer;
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 2
        for i in range(1, result.shape[0]):
            assert result.iloc[i].loc['average_price'] >= \
                   result.iloc[i - 1].loc['average_price']

    def test5(self):
        query = """
            SELECT *
            FROM shop.carpet_amount_by_address;
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 2
        for i in range(1, result.shape[0]):
            assert result.iloc[i].loc['total_carpet'] <= \
                   result.iloc[i - 1].loc['total_carpet']

    def test6(self):
        query = """
            SELECT *
            FROM shop.carpet_sales_by_category;
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 2
        for i in range(1, result.shape[0]):
            assert result.iloc[i].loc['total_sold'] <= \
                   result.iloc[i - 1].loc['total_sold']

    def end(self):
        self.cursor.close()
        self.conn.close()
