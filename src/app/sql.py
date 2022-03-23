import sqlite3


class Connection(object):
    DB_LOCATION = "sqlite_python.db"

    def __init__(self):
        self.connection = sqlite3.connect(self.DB_LOCATION)
        self.cur = self.connection.cursor()

    def __enter__(self):
        return self

    def close(self):
        self.connection.close()

    def execute(self, new_data):
        self.cur.execute(new_data)

    def commit(self):
        self.connection.commit()

    def get_user(self, login):
        select_query = f"""SELECT username, hashed_password FROM users WHERE username='{login}'"""
        self.execute(select_query)
        return self.cur.fetchone()

    def get_cache(self, img_string):
        select_query = f"""SELECT img_string, image FROM caching WHERE img_string='{img_string}'"""
        self.execute(select_query)
        return self.cur.fetchone()

    def add_cache(self, img_string, image):
        insert_query = f"""INSERT INTO caching (img_string, image)  VALUES  ('{img_string}', '{image}')"""
        self.execute(insert_query)
        self.commit()
        print('New cache created')

    #Exception handling and exiting
    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()




def connection():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        # sqlite_create_table_query = '''CREATE TABLE users (
        #                             id INTEGER PRIMARY KEY,
        #                             username TEXT NOT NULL unique,
        #                             hashed_password text NOT NULL);'''

        sqlite_insert_query = """INSERT INTO users
                                  (username, hashed_password)  VALUES  (kwaffle, '$2b$12$w9cNaVtJI1ofOlUUrBb3geFCnLB0N3hTX/j4.XUNrKk3uPvLpc7lK')"""

        cursor = sqlite_connection.cursor()
        # print("База данных подключена к SQLite")
        # cursor.execute(sqlite_insert_query)



        sqlite_connection.commit()
        print("Таблица SQLite создана")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
