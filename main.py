import sqlitedb
import datetime
from read import get_data
from dates import get_last_30_days
from datetime import datetime
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

class Form():
    def __init__(self, _root, tp):
        self.type = tp

        frame = ttk.Frame(_root, padding=10, borderwidth=1, relief=GROOVE)

        date_label = ttk.Label(master=frame, text="Дата")
        cat_label = ttk.Label(master=frame, text="Категория")
        sum_label = ttk.Label(master=frame, text="Сумма")

        self.date_entry = ttk.Combobox(master=frame, values=get_last_30_days(), state="readonly")
        self.date_entry.current(0)
        # date_entry.insert(0, '2025-mm-dd')

        if self.type == 1:
            cats = ['products', 'cafe', 'transport']
        else:
            cats = ['save_acc_%', 'advance', 'salary']

        self.cat_entry = ttk.Combobox(master=frame, values=cats, state="readonly")
        self.cat_entry.current(0)

        self.sum_entry = ttk.Entry(master=frame)
        self.button = ttk.Button(master=frame, text="GET", command=self.get_cash_flow)

        date_label.grid(row=0, column=0, padx=10)
        cat_label.grid(row=0, column=1, padx=10)
        sum_label.grid(row=0, column=2, padx=10)

        self.date_entry.grid(row=1, column=0, padx=10)
        self.cat_entry.grid(row=1, column=1, padx=10)
        self.sum_entry.grid(row=1, column=2, padx=10)
        self.button.grid(row=1, column=3, padx=10)

        frame.pack(anchor=CENTER, expand=0)

    def get_cash_flow(self):
        date = datetime.strptime((self.date_entry.get()), "%d %B %Y (%a)").date()
        date_format = date.strftime('%Y-%m-%d')

        cat = str(self.cat_entry.get())
        sm = int(self.sum_entry.get())

        if self.type == 1:
            sqlitedb.add_day_expenses(cat, sm, date_format)
        else:
            sqlitedb.add_day_income(cat, sm, date_format)

# frame3 = ttk.Frame(root, padding=10, borderwidth=1, relief=GROOVE)
expenses_frame = Form(root, 1)
income_frame = Form(root, 2)

# frame4 = ttk.Frame(root, padding=10, borderwidth=1, relief=GROOVE)

def make_expenses_window():
    Window("Расходы", sqlitedb.get_expenses())

def make_income_window():
    Window("Доходы", sqlitedb.get_income())

def make_deposits_window():
    WindowDep("Вклады", sqlitedb.get_deposits())

def make_graph():
    GraphWindow("График", sqlitedb.get_category_expenses())






button1 = ttk.Button(master=root, text="Расходы", command=make_expenses_window)
button1.pack(anchor=CENTER, expand=0)

button2 = ttk.Button(master=root, text="Доходы", command=make_income_window)
button2.pack(anchor=CENTER, expand=0)

button3 = ttk.Button(master=root, text="Вклады", command=make_deposits_window)
button3.pack(anchor=CENTER, expand=0)

button4 = ttk.Button(master=root, text="График", command=make_graph)
button4.pack(anchor=CENTER, expand=0)

############################

# date_label = ttk.Label(master=frame3, text="Дата")
# cat_label = ttk.Label(master=frame3, text="Категория")
# sum_label = ttk.Label(master=frame3, text="Сумма")
#
#
# date_entry = ttk.Combobox(master=frame3, values=get_last_30_days(), state="readonly")
# date_entry.current(0)
# # date_entry.insert(0, '2025-mm-dd')
#
# cats = ['products', 'cafe', 'transport']
# cat_entry = ttk.Combobox(master=frame3, values=cats, state="readonly")
# cat_entry.current(0)
#
# sum_entry = ttk.Entry(master=frame3)
# button5 = ttk.Button(master=frame3, text="GET", command=get_expense)
#
# date_label.grid(row=0, column=0, padx=10)
# cat_label.grid(row=0, column=1, padx = 10)
# sum_label.grid(row=0, column=2, padx = 10)
#
# date_entry.grid(row=1, column=0, padx=10)
# cat_entry.grid(row=1, column=1, padx = 10)
# sum_entry.grid(row=1, column=2, padx = 10)
# button5.grid(row=1, column=3, padx = 10)
#
# frame3.pack(anchor=CENTER, expand=0)

############################
#
# date_label2 = ttk.Label(master=frame4, text="Дата")
# cat_label2 = ttk.Label(master=frame4, text="Категория")
# sum_label2 = ttk.Label(master=frame4, text="Сумма")
#
# date_entry2 = ttk.Entry(master=frame4)
# date_entry2.insert(0, '2025-mm-dd')
#
# cats2 = ['save_acc_%', 'advance', 'salary']
# cat_entry2 = ttk.Combobox(master=frame4, values=cats2, state="readonly")
# cat_entry2.current(2)
#
# sum_entry2 = ttk.Entry(master=frame4)
# button6 = ttk.Button(master=frame4, text="GET", command=get_income)
#
# date_label2.grid(row=0, column=0, padx=10)
# cat_label2.grid(row=0, column=1, padx = 10)
# sum_label2.grid(row=0, column=2, padx = 10)
#
# date_entry2.grid(row=1, column=0, padx=10)
# cat_entry2.grid(row=1, column=1, padx = 10)
# sum_entry2.grid(row=1, column=2, padx = 10)
# button6.grid(row=1, column=3, padx = 10)
#
# frame4.pack(anchor=CENTER, expand=0)


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