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
            SELECT name, price
            FROM shop.carpet
            WHERE price < 1500
              AND amount > 1
            ORDER BY name;
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 2
        assert result.iloc[0].loc['price'] < 1500
        for i in range(1, result.shape[0]):
            assert result.iloc[i].loc['name'] >= \
                   result.iloc[i - 1].loc['name']
            assert result.iloc[i].loc['price'] < 1500

    def test2(self):
        query = """
            SELECT carpet.producer_id, 
                   p.name, 
                   p.country, 
                   count(carpet_id) AS carpet_number
            FROM shop.carpet
                     INNER JOIN shop.producer p
                                ON carpet.producer_id = p.producer_id
            GROUP BY carpet.producer_id, p.name, p.country
            HAVING count(carpet_id) > 1;
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 4
        for i in range(result.shape[0]):
            assert result.iloc[i].loc['carpet_number'] > 1

    def test3(self):
        query = """
            SELECT name,
                   category,
                   dense_rank() OVER (ORDER BY category) AS category_num
            FROM shop.carpet
                     INNER JOIN shop.carpet_description c
                                ON carpet.carpet_id = c.carpet_id;
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 3
        for i in range(1, result.shape[0]):
            assert result.iloc[i].loc['category_num'] >= \
                   result.iloc[i - 1].loc['category_num']

    def test4(self):
        query = """
            SELECT name,
                   colour,
                   count(c.carpet_id) OVER (PARTITION BY c.colour) AS colour_count
            FROM shop.carpet
                     INNER JOIN shop.carpet_description c
                                ON carpet.carpet_id = c.carpet_id;
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 3

        d = dict()
        for i in range(result.shape[0]):
            col = result.iloc[i].loc['colour']
            if col in d:
                d[col] += 1
            else:
                d[col] = 1

        for i in range(result.shape[0]):
            col = result.iloc[i].loc['colour']
            assert d[col] == result.iloc[i].loc['colour_count']


    def test5(self):
        query = """
            SELECT name,
                   category,
                   price,
                   first_value(price)
                   OVER (PARTITION BY category
                       ORDER BY price)
                       AS min_category_price
            FROM shop.carpet
                     INNER JOIN shop.carpet_description c
                                ON carpet.carpet_id = c.carpet_id;
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 4
        for i in range(result.shape[0]):
            assert result.iloc[i].loc['min_category_price'] <= \
                   result.iloc[i].loc['price']

    def test6(self):
        query = """
            SELECT name, address, date_from, date_to
            FROM shop.carpet
                     INNER JOIN shop.carpet_supply cs
                                ON carpet.carpet_id = cs.carpet_id
                     INNER JOIN shop.supply s
                                ON cs.supply_id = s.supply_id
            ORDER BY date_from
        """
        result = pd.read_sql(query, con=self.conn)
        assert result.shape[1] == 4
        assert result.iloc[0].loc['date_from'] <= result.iloc[0].loc['date_to']
        for i in range(1, result.shape[0]):
            assert result.iloc[i].loc['date_from'] >= \
                   result.iloc[i - 1].loc['date_from']
            assert result.iloc[i].loc['date_from'] <= result.iloc[i].loc['date_to']

    def end(self):
        self.cursor.close()
        self.conn.close()
