import sqlite3


def database_init():
    global connection
    global cursor
    connection = sqlite3.connect("database.db")  # коннект к БД
    cursor = connection.cursor()  # курсор для выполнения запросов

    if connection:
        print("Успешное подключение к БД")



def make_expenses():
    """ "Создание таблицы расходов" """
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                sum INTEGER,
                date TEXT NOT NULL
                )''')
    connection.commit()

def make_income():
    """ "Создание таблицы доходов" """
    cursor.execute('''CREATE TABLE IF NOT EXISTS income(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                sum INTEGER,
                date TEXT NOT NULL
                )''')
    connection.commit()

def make_deposits():
    """ "Создание таблицы вкладов" """
    cursor.execute('''CREATE TABLE IF NOT EXISTS deposits(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bank TEXT NOT NULL,
                sum INTEGER NOT NULL,
                percent REAL NOT NULL,
                date_from TEXT NOT NULL,
                date_to TEXT NOT NULL
                )''')
    connection.commit()


def add_day_expenses(cat, summa, data):
    cursor.execute(f"INSERT INTO expenses(category, sum, date) VALUES(?, ?, ?)", (cat, summa, data))
    connection.commit()
    if connection:
        print("Успешная вставка")

def add_day_income(cat, summa, data):
    cursor.execute(f"INSERT INTO income(category, sum, date) VALUES(?, ?, ?)", (cat, summa, data))
    connection.commit()
    if connection:
        print("Успешная вставка")

def add_deposit(bank, sum, percent, date_from, date_to):
    cursor.execute(f"INSERT INTO deposits(bank, sum, percent, date_from, date_to) VALUES(?, ?, ?, ?, ?)", (bank, sum, percent, date_from, date_to))
    connection.commit()
    if connection:
        print("Успешная вставка")

def get_expenses():
    cursor.execute("SELECT category, sum, date FROM expenses")
    a = cursor.fetchall()
    return a

def get_income():
    cursor.execute("SELECT category, sum, date FROM income")
    a = cursor.fetchall()
    return a

def get_deposits():
    cursor.execute("SELECT bank, sum, percent, date_from, date_to FROM deposits")
    a = cursor.fetchall()
    return a


def get_day_expenses(cat, data):
    cursor.execute("SELECT SUM(sum) FROM expenses WHERE category = ? AND date = ?", (cat, data))
    b = cursor.fetchone()
    print(b)

def get_total_category_expenses(cat):
    cursor.execute("SELECT SUM(sum) FROM expenses WHERE category = ?", (cat,))
    b = cursor.fetchone()
    print(b)

def get_category_expenses():
    cursor.execute("SELECT category, SUM(sum) FROM expenses GROUP BY category")
    b = cursor.fetchall()
    return b

# месячный подсчет расходов по одной категории
def get_month_category_sum(cat, date_from, date_to):
    cursor.execute("SELECT SUM(sum) FROM expenses WHERE category = ? AND date BETWEEN ? AND ?", (cat, date_from, date_to))
    b = cursor.fetchone()
    return b