import sqlitedb
import datetime
from read import get_data
from dates import get_last_30_days, get_last_30_days_unformat
from datetime import datetime
from tkinter import *
from tkinter import ttk

from window import Window, WindowDep, GraphWindow, WW
from config import window_size

from forms import Form, DepositForm

# Инициализация БД
sqlitedb.database_init()
sqlitedb.make_expenses()    # таблица расходов
sqlitedb.make_income()      # таблица доходов
sqlitedb.make_deposits()    # таблица вкладов
######################################################

# Создание GUI
root = Tk()
root.title("")
root.geometry(window_size)
######################################################

# Добавление форм на стартовое меню
expenses_frame = Form(root, 1)      # Форма расходов
income_frame = Form(root, 2)        # Форма доходов
deposit_frame = DepositForm(root)   # Форма вкладов
######################################################


def make_expenses_window():
    Window("Расходы", sqlitedb.get_expenses())

def make_income_window():
    Window("Доходы", sqlitedb.get_income())

def make_deposits_window():
    WindowDep("Вклады", sqlitedb.get_deposits())

def make_graph():
    GraphWindow("График", sqlitedb.get_category_expenses())

def make_table():
    ww = WW("TEST", sqlitedb.get_cats())
    a = get_last_30_days_unformat()
    for el in a:
        ww.insert(sqlitedb.get_day_expenses(el.strftime('%Y-%m-%d')))


# Добавление кнопок на стартовое меню
button1 = ttk.Button(master=root, text="Расходы", command=make_expenses_window)
button1.pack(anchor=CENTER, expand=0)

button2 = ttk.Button(master=root, text="Доходы", command=make_income_window)
button2.pack(anchor=CENTER, expand=0)

button3 = ttk.Button(master=root, text="Вклады", command=make_deposits_window)
button3.pack(anchor=CENTER, expand=0)

button4 = ttk.Button(master=root, text="График", command=make_graph)
button4.pack(anchor=CENTER, expand=0)

button5 = ttk.Button(master=root, text="Таблица", command=make_table)
button5.pack(anchor=CENTER, expand=0)
######################################################

root.mainloop()






########################################################################## Занесение данных в базу
# content = get_data(5, 'products')
# content = get_data(10, 'transport')
# content = get_data(12, 'cafe')
# content = get_data(8, 'gifts')
# content = get_data(13, 'other')
# content = get_data(14, 'clothes')
# content = get_data(15, 'shoes')
# content = get_data(16, 'health')
# for el in content:
#     sqlitedb.add_day_expenses(el[0], el[1], el[2])

# content = get_data(20, "save_acc_%")
# content = get_data(24, "advance")
# content = get_data(27, "salary")
#
# for el in content:
#     sqlitedb.add_day_income(el[0], el[1], el[2])

# sqlitedb.add_deposit("ВТБ", 300000, 15.6, "2025-10-06", '2026-02-03')
# sqlitedb.add_deposit("ВТБ", 585000, 15.6, "2025-10-06", '2026-02-03')
# sqlitedb.add_deposit("Сбер", 300000, 16, "2025-08-12", '2025-12-12')
# sqlitedb.add_deposit("Сбер", 250000, 16, "2025-11-08", '2026-02-08')
##########################################################################