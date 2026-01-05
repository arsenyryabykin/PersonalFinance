
from tkinter import *
from tkinter import ttk

from dates import get_last_30_days, get_last_30_days_unformat
import sqlitedb
import datetime

class Form():
    '''
    Класс создания формы для занесения ежедневных расходов и доходов по категориям (на стартовое меню)

    Параметры:
    tp (int): тип формы (1 - расходы, 2 - доходы)
    '''
    def __init__(self, _root, tp):
        self.type = tp

        frame = ttk.Frame(_root, padding=10, borderwidth=1, relief=GROOVE)

        date_label = ttk.Label(master=frame, text="Дата")
        cat_label = ttk.Label(master=frame, text="Категория")
        sum_label = ttk.Label(master=frame, text="Сумма")

        self.date_entry = ttk.Combobox(master=frame, values=get_last_30_days(), state="readonly")
        self.date_entry.current(0)

        if self.type == 1:
            # cats = ['products', 'cafe', 'transport']
            cats = sqlitedb.get_cats()
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

#################################################################################
#################################################################################



class DepositForm():
    '''
    Класс создания формы для добавления вклада (на стартовое меню)
    '''
    def __init__(self, _root):
        frame = ttk.Frame(_root, padding=10, borderwidth=1, relief=GROOVE)

        bank_label = ttk.Label(master=frame, text="Банк")
        deposit_label = ttk.Label(master=frame, text="Сумма")
        percent_label = ttk.Label(master=frame, text="Процент")
        date_from_label = ttk.Label(master=frame, text="Дата открытия (YY-mm-dd)")
        date_to_label = ttk.Label(master=frame, text="Дата закрытия (YY-mm-dd)")

        self.bank_entry = ttk.Combobox(master=frame, values=["Сбер", "ВТБ"], state="readonly")
        self.bank_entry.current(0)

        self.deposit_entry = ttk.Entry(master=frame)

        self.percent_entry = ttk.Entry(master=frame)

        self.date_from_entry = ttk.Entry(master=frame)
        self.date_to_entry = ttk.Entry(master=frame)

        self.button = ttk.Button(master=frame, text="GET", command=self.get_deposit)


        bank_label.grid(row=0, column=0, padx=10)
        deposit_label.grid(row=0, column=1, padx=10)
        percent_label.grid(row=0, column=2, padx=10)
        date_from_label.grid(row=0, column=3, padx=10)
        date_to_label.grid(row=0, column=4, padx=10)

        self.bank_entry.grid(row=1, column=0, padx=10)
        self.deposit_entry.grid(row=1, column=1, padx=10)
        self.percent_entry.grid(row=1, column=2, padx=10)
        self.date_from_entry.grid(row=1, column=3, padx=10)
        self.date_to_entry.grid(row=1, column=4, padx=10)

        self.button.grid(row=1, column=5, padx=10)

        frame.pack(anchor=CENTER, expand=0)

    def get_deposit(self):
        bank = str(self.bank_entry.get())
        dep = int(self.deposit_entry.get())
        percent = float(self.percent_entry.get())
        date_from = str(self.date_from_entry.get())
        date_to = str(self.date_to_entry.get())

        sqlitedb.add_deposit(bank, dep, percent, date_from, date_to)