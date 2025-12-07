from tkinter import *
from tkinter import ttk

class Window(Tk):
    def __init__(self, title_, content):
        super().__init__()

        self.title(str(title_))
        self.geometry("1000x1000")
        self.update_idletasks()

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
        tree.column("#1", stretch=NO, anchor=N)
        tree.column("#2", stretch=NO, anchor=N)
        tree.column("#3", stretch=NO, anchor=N)
        # #
        for person in content:
            tree.insert("", END, values=person)


class WindowDep(Tk):
    def __init__(self, title_, content):
        super().__init__()

        self.title(str(title_))
        self.geometry("600x250")
        self.update_idletasks()


        columns = ("bank", "sum", "percent", "date_from", "date_to")
        #
        tree = ttk.Treeview(master=self, show="headings", columns=columns)
        tree.pack(fill=NONE, expand=1)
        # tree.grid(row=0, column=0, sticky="nsew")
        #
        tree.heading("bank", text="Банк", anchor=S)
        tree.heading("sum", text="Сумма", anchor=S)
        tree.heading("percent", text="Процент", anchor=S)
        tree.heading("date_from", text="Дата открытия", anchor=S)
        tree.heading("date_to", text="Дата закрытия", anchor=S)
        #
        tree.column("#1", stretch=NO, anchor=N)
        tree.column("#2", stretch=NO, anchor=N)
        tree.column("#3", stretch=NO, anchor=N)
        tree.column("#4", stretch=NO, anchor=N)
        tree.column("#5", stretch=NO, anchor=N)
        # #
        for el in content:
            tree.insert("", END, values=el)




