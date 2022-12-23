import os

import pymysql


class Database:
    def __init__(self):
        db_settings = {
            "host": os.getenv("MYSQL_HOST"),
            "port": 3306,
            "user": "root",
            "password": os.getenv("MYSQL_PASSWORD"),
            "db": "dc_lottery",
            "charset": "utf8",
        }

        self.conn = pymysql.connect(**db_settings)
        self.create_schema()

    def create_schema(self):
        with self.conn.cursor() as cursor:
            sql = """
            CREATE TABLE IF NOT EXISTS Members (
                Name varchar(255) UNIQUE NOT NULL
            );
            """
            cursor.execute(sql)
            self.conn.commit()

    def insert(self, name):
        with self.conn.cursor() as cursor:
            sql = """
            INSERT INTO Members (Name) VALUES (%s);
            """
            cursor.execute(sql, (name))
            self.conn.commit()

    def delete(self, name):
        with self.conn.cursor() as cursor:
            sql = """
            DELETE FROM Members WHERE Name = %s;
            """
            cursor.execute(sql, (name))
            self.conn.commit()

    def select(self):
        with self.conn.cursor() as cursor:
            sql = """
            SELECT * FROM Members;
            """
            cursor.execute(sql)
            self.conn.commit()
            return cursor.fetchall()
