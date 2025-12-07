import sqlitedb

from read import get_data

from tkinter import *
from tkinter import ttk

from window import Window, WindowDep

sqlitedb.database_init()
sqlitedb.make_expenses()
sqlitedb.make_income()
sqlitedb.make_deposits()

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





root = Tk()
root.title("")
root.geometry("200x200")
root.rowconfigure(index=0, weight=1)
root.columnconfigure(index=0, weight=1)


# b = sqlitedb.show()

def make_expenses_window():
    Window("Расходы", sqlitedb.get_expenses())

def make_income_window():
    Window("Доходы", sqlitedb.get_income())

def make_deposits_window():
    WindowDep("Вклады", sqlitedb.get_deposits())


button1 = ttk.Button(text="Расходы", command=make_expenses_window)
button1.pack(anchor=CENTER, expand=1)

button2 = ttk.Button(text="Доходы", command=make_income_window)
button2.pack(anchor=CENTER, expand=0)

button3 = ttk.Button(text="Вклады", command=make_deposits_window)
button3.pack(anchor=CENTER, expand=1)



root.mainloop()




# while(True):
#     print("0 - EXIT\n1 - Ввод расхода\n2 - Вывод\n")
#     T = int(input())
#
#     if T == 0:
#         print("EXIT")
#         break
#
#     if T == 1:
#         print("Категория: ")
#         category_name = str(input())
#         print("Сумма: ")
#         summa = int(input())
#         print("Дата: (xx-xx-xx) ")
#         data = str(input())
#
#         sqlitedb.add_day_expenses(category_name, summa, data)
#
#         print(category_name, summa, data)
#         continue
# #
#     if T == 2:
#         sqlitedb.show()
