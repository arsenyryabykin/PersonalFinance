from tkinter import *
from tkinter import ttk

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import sqlitedb

matplotlib.use("TkAgg")

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

class GraphWindow(Tk):
    def __init__(self, title_, data):
        super().__init__()

        self.title(str(title_))
        self.geometry("500x500")
        self.update_idletasks()

        frame = ttk.Frame(self, padding=10, borderwidth=1, relief=GROOVE)
        frame.pack(side=TOP, expand=1, fill=BOTH)
        frame.pack_propagate(False)


        frame2 = ttk.Frame(self, padding=10, borderwidth=1, relief=GROOVE)
        frame2.pack(side=BOTTOM, expand=0, fill=BOTH)
        frame2.config(height=100)
        frame2.pack_propagate(False)

        x = [a[0] for a in data]
        y = [b[1] for b in data]



        figure = Figure(figsize=(10, 10), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, frame)
        # plt = figure.add_subplot(1, 2, 1)
        # plt.bar(x, y)



        plt2 = figure.add_subplot(1,1,1)
        d = [(f"2024-{m}-01", f"2024-{m}-31") for m in ['02', '03', '04', '05', '06', '07', '08', '09', '10']]
        xx = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
        yy = [sqlitedb.get_month_category_sum('products', el[0], el[1])[0] for el in d]
        plt2.bar(xx, yy)

        figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


        button3 = ttk.Label(master=frame2, text="Вклады")
        button3.pack(anchor=CENTER, expand=0)

