import os
import pandas as pd
import psycopg2 as pg
from faker import Faker
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


if __name__ == '__main__':
    conn = set_connection()

    cur = conn.cursor()

    # Инициализация Faker
    fake = Faker()

    # Сгенерировать данные для таблицы shop.producer
    for i in range(10):
        producer_name = fake.company()
        producer_country = fake.country()
        try:
            cur.execute("INSERT INTO shop.producer (name, country) VALUES (%s, %s)",
                        (producer_name, producer_country))
            conn.commit()
        except pg.IntegrityError:
            # Обрабатываем ошибку
            conn.rollback()

    # Получить список всех производителей
    cur.execute("SELECT producer_id FROM shop.producer")
    producer_ids = [row[0] for row in cur.fetchall()]

    # Сгенерировать данные для таблицы shop.carpet
    for i in range(100):
        # Вставка данных в таблицу shop.carpet
        carpet_producer_id = fake.random_element(elements=producer_ids)
        carpet_name = fake.text(max_nb_chars=50)
        carpet_price = fake.pyint(min_value=10, max_value=1000)
        carpet_amount = fake.pyint(min_value=0, max_value=100)
        try:
            cur.execute("INSERT INTO shop.carpet (producer_id, name, price, amount) VALUES (%s, %s, %s, %s)",
                        (carpet_producer_id, carpet_name, carpet_price, carpet_amount))
            conn.commit()
        except pg.IntegrityError:
            # Обрабатываем ошибку
            conn.rollback()

        # Получение текущего значения для carpet_id
        cur.execute("SELECT currval('shop.carpet_carpet_id_seq')")
        carpet_id = cur.fetchone()[0]

        # Вставка данных в таблицу shop.carpet_description
        carpet_category = fake.word()
        carpet_length = fake.pyint(min_value=10, max_value=100)
        carpet_width = fake.pyint(min_value=10, max_value=100)
        carpet_colour = fake.color_name()
        try:
            cur.execute(
                "INSERT INTO shop.carpet_description (carpet_id, category, length, width, colour) VALUES (%s, %s, %s, %s, %s)",
                (carpet_id, carpet_category, carpet_length, carpet_width, carpet_colour))
            conn.commit()
        except pg.IntegrityError:
            # Обрабатываем ошибку
            conn.rollback()

    # Закрытие соединения с БД
    cur.close()
    conn.close()
