import sqlitedb

from read import get_data

from tkinter import *
from tkinter import ttk

sqlitedb.database_init()
sqlitedb.make_expenses()

# content = get_data(5, 'products')
# for el in content:
#     sqlitedb.add_day_expenses(el[0], el[1], el[2])
#
# content = get_data(10, 'transport')
# for el in content:
#     sqlitedb.add_day_expenses(el[0], el[1], el[2])
#
# content = get_data(12, 'cafe')
# for el in content:
#     sqlitedb.add_day_expenses(el[0], el[1], el[2])

class Window(Tk):
    def __init__(self, title_, content):
        super().__init__()

        self.title(str(title_))
        self.geometry("600x300")

        columns = ("category", "sum", "date")
        #
        tree = ttk.Treeview(master=self, show="headings", columns=columns)
        tree.pack(fill=BOTH, expand=1)
        # tree.grid(row=0, column=0, sticky="nsew")
        #
        tree.heading("category", text="Категория", anchor=S)
        tree.heading("sum", text="Сумма", anchor=S)
        tree.heading("date", text="Дата", anchor=S)
        #
        tree.column("#1", stretch=YES, anchor=N)
        tree.column("#2", stretch=YES, anchor=N)
        tree.column("#3", stretch=YES, anchor=N)
        # #
        for person in content:
            tree.insert("", END, values=person)



root = Tk()
root.title("")
root.geometry("200x200")
root.rowconfigure(index=0, weight=1)
root.columnconfigure(index=0, weight=1)


# b = sqlitedb.show()

def make_expenses_window():
    Window("Расходы", sqlitedb.show())


button1 = ttk.Button(text="Расходы", command=make_expenses_window)
button1.pack(anchor=CENTER, expand=1)

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
