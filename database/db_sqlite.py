import sqlite3



class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())
    
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()

        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()

        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data



    def create_category_table(self):
        sql = """CREATE TABLE IF NOT EXISTS Categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(250),
        image TEXT
        )"""
        self.execute(sql, commit=True)

    def create_product_table(self):
        sql = """CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(300),
        description VARCHAR(3000),
        image TEXT,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES Categories (id) ON DELETE CASCADE
        )"""
        self.execute(sql, commit=True)

    def create_users_table(self):
        sql = """CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER NOT NULL UNIQUE,
        username VARCHAR(255),
        language VARCHAR(10),
        registered_date TEXT
        )"""
        self.execute(sql, commit=True)

    def create_orders_table(self):
        sql = """CREATE TABLE IF NOT EXISTS Orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product_id INTEGER,
        price REAL,
        type_product VARCHAR(10),
        quantity INTEGER,
        date_time TEXT,
        location TEXT,
        FOREIGN KEY (location) REFERENCES Locations (location),
        FOREIGN KEY (user_id) REFERENCES Users (id),
        FOREIGN KEY (product_id) REFERENCES Products (id)
        )"""
        self.execute(sql, commit=True)

    def create_type_table(self):
        sql = """CREATE TABLE IF NOT EXISTS Types (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type_product VARCHAR(10),
        price REAL,
        product_id INTEGER,
        FOREIGN KEY (product_id) REFERENCES Products (id) ON DELETE CASCADE
        )"""
        self.execute(sql, commit=True)

    def create_location_table(self):
        sql = """CREATE TABLE IF NOT EXISTS Locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER
        location VARCHAR(255),
        latitude TEXT,
        longitude TEXT,
        location TEXT,
        FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE
        )"""
        self.execute(sql, commit=True)



    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)



    def add_category(self, category_name, image):
        sql = """INSERT INTO Categories (name, image) VALUES
        (?, ?)
        """
        self.execute(sql, parameters=(category_name, image), commit=True)

    def add_product(self, name, image, category_name, description=None):
        sql = """INSERT INTO Products (name, image, category_id, description) VALUES
        (?, ?, (SELECT id FROM Categories WHERE name = ?), ?)
        """
        self.execute(sql, parameters=(name, image, category_name, description), commit=True)

    def add_user(self, telegram_id, username, language, registered_date):
        sql = """INSERT OR IGNORE INTO Users (telegram_id, username, language, registered_date) VALUES
        (?, ?, ?, ?)
        """
        self.execute(sql, parameters=(telegram_id, username, language, registered_date), commit=True)

    def add_order(self, telegram_id, product_name, price, type_product, quantity, data_time, location):
        sql1 = """SELECT id FROM Orders WHERE user_id = (SELECT id FROM Users WHERE telegram_id = ?) AND product_id = (SELECT id FROM Products WHERE name = ?) AND type_product = ?"""
        data = self.execute(sql1, parameters=(telegram_id, product_name, type_product), fetchall=True)
        if data == []:
            sql3 = """INSERT INTO Orders (user_id, product_id, price, type_product, quantity, date_time, location)
                    SELECT (SELECT id FROM Users WHERE telegram_id = ?),
                        (SELECT id FROM Products WHERE name = ?),
                        ?, ?, ?, ?, ?"""
            self.execute(sql3, parameters=(telegram_id, product_name, price, type_product, quantity, data_time, location), commit=True)
        elif data is not None:
            sql2 = '''UPDATE Orders SET quantity = ?
                WHERE user_id = (SELECT id FROM Users WHERE telegram_id = ?) AND product_id = (SELECT id FROM Products WHERE name = ?) AND type_product = ?'''
            self.execute(sql2, parameters=(quantity, telegram_id, product_name, type_product), commit=True)

    def add_type(self, type_product, price, product_id):
        sql = """INSERT INTO Types (type_product, price, product_id) VALUES
        (?, ?, (SELECT id FROM Products WHERE id = ?))"""
        self.execute(sql, parameters=(type_product, price, product_id), commit=True)

    def add_location(self, telegram_id, latitude, longitude, location):
        sql = """INSERT INTO Locations (user_id, latitude, longitude, location) VALUES
        ((SELECT id FROM Users WHERE telegram_id = ?), ?, ?, ?)"""
        self.execute(sql, parameters=(telegram_id, latitude, longitude, location), commit=True)



    def get_all_categories(self):
        sql = """SELECT name FROM Categories"""
        data = self.execute(sql, fetchall=True)
        return data

    def get_category_image(self, category_name):
        sql = """SELECT image FROM Categories WHERE name = ?"""
        data = self.execute(sql, parameters=(category_name,), fetchone=True)
        if data is not None:
            return data
        else:
            return None

    def get_all_products(self, category_name):
        sql = """SELECT name FROM Products WHERE category_id = (SELECT id FROM Categories WHERE name = ?)"""
        data = self.execute(sql, (category_name,), fetchall=True)
        return data

    def get_all_locations(self, telegram_id):
        sql = """SELECT location FROM Locations WHERE user_id = (SELECT id FROM Users WHERE telegram_id = ?)"""
        data = self.execute(sql, (telegram_id,), fetchall=True)
        return data

    def get_all_categories_before_location(self, location):
        sql = """SELECT location FROM Locations WHERE location = ?"""
        data = self.execute(sql, parameters=(location,), fetchall=True)
        if data is not None:
            return True
        else:
            return None

    def get_product_image(self, product_name):
        sql = """SELECT image FROM Products WHERE name = ?"""
        data = self.execute(sql, parameters=(product_name,), fetchone=True)
        return data
    
    def get_type(self, product_name):
        sql = """SELECT type_product, price FROM Types WHERE product_id = (SELECT id FROM Products WHERE name = ?)"""
        data = self.execute(sql, parameters=(product_name,), fetchall=True)
        return data
    
    def get_product_description(self, product_name):
        sql = """SELECT description FROM Products WHERE name = ?"""
        data = self.execute(sql, parameters=(product_name,), fetchall=True)
        print(data)
        if data == [(None,)] or data == []:
            return
        else:
            return data[0][0]

    def get_all_orders(self, telegram_id):
        sql = """SELECT user_id, product_id, price, type_product, quantity FROM Orders WHERE user_id = (SELECT id FROM Users WHERE telegram_id = ?)"""
        data = self.execute(sql, parameters=(telegram_id,), fetchall=True)
        return data

    def get_product_name(self, product_id):
        sql = """SELECT name FROM Products WHERE id = ?"""
        data = self.execute(sql, parameters=(product_id,), fetchone=True)
        return data

    def get_ordered_product_price(self, product_id, type_product):
        sql = """SELECT price FROM Orders WHERE product_id = ? AND type_product = ?"""
        data = self.execute(sql, parameters=(product_id, type_product), fetchone=True)
        return data

    def get_ordered_product_price2(self, product_id):
        sql = """SELECT price FROM Orders WHERE product_id = ?"""
        data = self.execute(sql, parameters=(product_id,), fetchone=True)
        return data

    def get_product_price(self, product_name):
        sql = """SELECT price FROM Types WHERE product_id = (SELECT id FROM Products WHERE name = ?)"""
        data = self.execute(sql, parameters=(product_name,), fetchone=True)
        return data

    def get_order_type_product(self, product_id, price):
        sql = """SELECT type_product FROM Orders WHERE product_id = ? AND price = ?"""
        data = self.execute(sql, parameters=(product_id, price), fetchone=True)
        if data is not None:
            return data
        elif data == None:
            return None

    def delete_all_orders(self, telegram_id):
        sql = """DELETE FROM Orders WHERE user_id = (SELECT id FROM Users WHERE telegram_id = ?)"""
        self.execute(sql, parameters=(telegram_id), commit=True)

    def get_all_orders_price(self, telegram_id):
        sql = """SELECT SUM(price * quantity) FROM Orders WHERE user_id = (SELECT id FROM Users WHERE telegram_id = ?)"""
        data = self.execute(sql, parameters=(telegram_id,), fetchone=True)
        return data[0]

    def delete_ordered_product(self, product_name, type_product: None):
        if type_product is not None:
            sql = """DELETE FROM Orders WHERE product_id = (SELECT id FROM Products WHERE name = ?) AND type_product = ?"""
            self.execute(sql, parameters=(product_name, type_product), commit=True)
        else:
            sql = """DELETE FROM Orders WHERE product_id = (SELECT id FROM Products WHERE name = ?)"""
            self.execute(sql, parameters=(product_name,), commit=True)



def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
from datetime import timezone