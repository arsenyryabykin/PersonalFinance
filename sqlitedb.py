import sqlite3


def database_init():
    global connection
    global cursor
    connection = sqlite3.connect("database.db")  # коннект к БД
    cursor = connection.cursor()  # курсор для выполнения запросов

    if connection:
        print("Успешное подключение к БД")


# Создание таблицы расходов на текущий месяц
def make_expenses():
    # cursor.execute('''DROP TABLE IF EXISTS expenses''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                sum INTEGER NOT NULL,
                date TEXT NOT NULL
                )''')

    # i = [(1,),(2,),(3,)]
    # cursor.executemany("INSERT INTO expenses(day) VALUES(?)", i)

    connection.commit()

def add_day_expenses(cat, summa, data):
    cursor.execute(f"INSERT INTO expenses(category, sum, date) VALUES(?, ?, ?)", (cat, summa, data))
    connection.commit()
    if connection:
        print("Успешная вставка")

def show():
    cursor.execute("SELECT * from expenses")
    print(cursor.fetchall())


def get_day_expenses(cat, data):
    cursor.execute("SELECT SUM(sum) FROM expenses WHERE category = ? AND date = ?", (cat, data))
    b = cursor.fetchone()
    print(b)

def get_total_category_expenses(cat):
    cursor.execute("SELECT SUM(sum) FROM expenses WHERE category = ?", (cat,))
    b = cursor.fetchone()
    print(b)