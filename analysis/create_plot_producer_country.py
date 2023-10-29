import os
import pandas as pd
import psycopg2 as pg
from faker import Faker
from dataclasses import dataclass
import matplotlib.pyplot as plt


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


if __name__ == '__main__':
    conn = set_connection()

    cur = conn.cursor()

    # SQL-запрос для получения количества ковров, произведенных каждой страной производителем
    query = """
    SELECT p.country, count(c.carpet_id)
    FROM shop.producer p
    LEFT JOIN shop.carpet c ON p.producer_id = c.producer_id
    GROUP BY p.country;
    """

    # Выполнение SQL-запроса и получение результатов
    cur.execute(query)
    rows = cur.fetchall()

    # Построение круговой диаграммы
    labels = [row[0] for row in rows]
    sizes = [row[1] for row in rows]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Страны производителей ковров")
    plt.axis('equal')
    plt.show()

    # Закрытие соединения с БД
    cur.close()
    conn.close()
