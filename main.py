import sqlitedb
import datetime
from read import get_data

from tkinter import *
from tkinter import ttk

from window import Window, WindowDep, GraphWindow

# Инициализация БД
sqlitedb.database_init()
sqlitedb.make_expenses()
sqlitedb.make_income()
sqlitedb.make_deposits()





# Создание GUI
root = Tk()
root.title("")
root.geometry("600x500")
root.rowconfigure(index=0, weight=1)
root.columnconfigure(index=0, weight=1)

# notebook = ttk.Notebook()
# notebook.pack(expand=0, fill=BOTH)
#
# frame1 = ttk.Frame(notebook)
# frame2 = ttk.Frame(notebook)
#
# frame1.pack(fill=BOTH, expand=1)
# frame2.pack(fill=BOTH, expand=1)
#
# notebook.add(frame1, text="aaa")
# notebook.add(frame2, text="bbb")

frame3 = ttk.Frame(root, padding=10, borderwidth=1, relief=GROOVE)

def make_expenses_window():
    Window("Расходы", sqlitedb.get_expenses())

def make_income_window():
    Window("Доходы", sqlitedb.get_income())

def make_deposits_window():
    WindowDep("Вклады", sqlitedb.get_deposits())

def make_graph():
    GraphWindow("График", sqlitedb.get_category_expenses())

def get():
    date = str(date_entry.get())
    cat = str(cat_entry.get())
    sm = int(sum_entry.get())

    sqlitedb.add_day_expenses(cat, sm, date)


button1 = ttk.Button(master=root, text="Расходы", command=make_expenses_window)
button1.pack(anchor=CENTER, expand=0)

button2 = ttk.Button(master=root, text="Доходы", command=make_income_window)
button2.pack(anchor=CENTER, expand=0)

button3 = ttk.Button(master=root, text="Вклады", command=make_deposits_window)
button3.pack(anchor=CENTER, expand=0)

button4 = ttk.Button(master=root, text="График", command=make_graph)
button4.pack(anchor=CENTER, expand=0)

date_label = ttk.Label(master=frame3, text="Дата")
cat_label = ttk.Label(master=frame3, text="Категория")
sum_label = ttk.Label(master=frame3, text="Сумма")

date_entry = ttk.Entry(master=frame3)
date_entry.insert(0, '2025-mm-dd')

cats = ['products', 'cafe', 'transport']
cat_entry = ttk.Combobox(master=frame3, values=cats, state="readonly")
cat_entry.current(0)


sum_entry = ttk.Entry(master=frame3)
button5 = ttk.Button(master=frame3, text="GET", command=get)

date_label.grid(row=0, column=0, padx=10)
cat_label.grid(row=0, column=1, padx = 10)
sum_label.grid(row=0, column=2, padx = 10)

date_entry.grid(row=1, column=0, padx=10)
cat_entry.grid(row=1, column=1, padx = 10)
sum_entry.grid(row=1, column=2, padx = 10)
button5.grid(row=1, column=3, padx = 10)

frame3.pack(anchor=CENTER, expand=1)


# date_entry.pack(anchor=CENTER)
# cat_entry.pack(anchor=CENTER)
# sum_entry.pack(anchor=CENTER)
# button5.pack(anchor=CENTER, expand=0)

root.mainloop()



##########################################################################
# content = get_data(5, 'products')
# content = get_data(10, 'transport')
# content = get_data(12, 'cafe')
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