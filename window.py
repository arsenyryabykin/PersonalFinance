from tkinter import *
from tkinter import ttk

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import sqlitedb

matplotlib.use("TkAgg")

d = {'date':'Дата','cafe':'Кафе', 'clothes':'Одежда', 'gifts':'Подарки', 'health':'Здоровье', 'other':'Другое', 'products':'Продукты', 'shoes':'Обувь', 'transport':'Транспорт', 'total':'Итого'}

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

class WW(Tk):
    # TODO: реализовать табличку расходов последних 30 дней"
    def __init__(self, title_, cats):
        super().__init__()

        self.count = 0

        print(cats)

        self.title(str(title_))
        self.geometry("1000x500")

        self.columns = ['date']
        self.columns += cats
        self.columns.append('total')

        print(self.columns)

        self.tree = ttk.Treeview(master=self, show="headings", columns=self.columns)
        self.tree.pack(fill=Y, expand=1, anchor=CENTER)
        for cat in self.columns:
            self.tree.heading(cat, text=d[cat], anchor=S)

        for i in range(1, len(self.columns) + 1):
            self.tree.column("#" + str(i), stretch=YES, width = 70, anchor=CENTER)

        self.tree.tag_configure("white", background='white')
        self.tree.tag_configure("blue", background='lightblue')

    def insert(self, day_exp):
        print(day_exp)
        insert_data = ['', '', '', '', '', '', '', '', '', '']
        insert_data[0] = day_exp[0][0]
        for i in range(1, len(self.columns)):
            for exp in day_exp:
                ind = self.columns.index(exp[1])
                insert_data[ind] = exp[2]

        if self.count % 2 == 0:
            self.tree.insert("", 0, values=insert_data, tags=('white',))
        else:
            self.tree.insert("", 0, values=insert_data, tags=('blue',))
        self.count += 1

class WindowDep(Tk):
    def __init__(self, title_, content):
        super().__init__()

        self.title(str(title_))
        self.geometry("900x400")
        self.update_idletasks()

        frame = ttk.Frame(self, padding=10, borderwidth=1, relief=GROOVE)

        columns = ("bank", "sum", "percent", "date_from", "date_to")
        #
        tree = ttk.Treeview(master=frame, show="headings", columns=columns)
        tree.pack(fill=BOTH, expand=1)
        # tree.grid(row=0, column=0)
        #
        tree.heading("bank", text="Банк", anchor=S)
        tree.heading("sum", text="Сумма", anchor=S)
        tree.heading("percent", text="Процент", anchor=S)
        tree.heading("date_from", text="Дата открытия", anchor=S)
        tree.heading("date_to", text="Дата закрытия", anchor=S)
        #
        tree.column("#1", stretch=YES, anchor=N)
        tree.column("#2", stretch=YES, anchor=N)
        tree.column("#3", stretch=YES, anchor=N)
        tree.column("#4", stretch=YES, anchor=N)
        tree.column("#5", stretch=YES, anchor=N)
        # #
        for el in content:
            tree.insert("", END, values=el)

        tmp_frame = ttk.Frame(self, padding=10, borderwidth=1, relief=GROOVE)
        label1 = ttk.Label(master=tmp_frame, text="Всего средств на вкладах")
        label1.grid(row=0, column=0)
        label2 = ttk.Label(master=tmp_frame, text=sqlitedb.get_sum_dep())
        label2.grid(row=0, column=1)



        frame.pack(anchor=W, expand=0)
        tmp_frame.pack(anchor=W, expand=1, fill=BOTH)

class GraphWindow(Tk):
    # FIXME: asfasfsf
    def __init__(self, title_, data):
        super().__init__()

        self.title(str(title_))
        self.geometry("1000x800")
        self.update_idletasks()

        ####################
        main_frame1 = ttk.Frame(self, padding=10, borderwidth=1, relief=RIDGE)

        frame1 = ttk.Frame(main_frame1, padding=10, borderwidth=1, relief=GROOVE)
        frame1.pack(side=TOP, expand=1, fill=BOTH)
        frame1.pack_propagate(False)

        self.figure1 = Figure(figsize=(10, 10), dpi=100)
        self.figure_canvas1 = FigureCanvasTkAgg(self.figure1, frame1)
        self.figure_canvas1.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        x = [a[0] for a in data]
        y = [b[1] for b in data]

        self.ax1 = self.figure1.add_subplot(1, 1, 1)
        self.ax1.bar(x, y, color="red")
        self.ax1.set_title("Траты по категориям")
        self.ax1.set_xticks(ticks=x)
        self.ax1.set_xticklabels(x, rotation=45)

        frame2 = ttk.Frame(main_frame1, padding=10, borderwidth=1, relief=GROOVE)
        frame2.pack(side=BOTTOM, expand=0, fill=BOTH)
        frame2.config(height=100)
        frame2.pack_propagate(False)

        button3 = ttk.Button(master=frame2, text="Вклады",command=self._change)
        button3.pack(anchor=CENTER, expand=0)

        ####################

        main_frame2 = ttk.Frame(self, padding=10, borderwidth=1, relief=RIDGE)

        frame3 = ttk.Frame(main_frame2, padding=10, borderwidth=1, relief=GROOVE)
        frame3.pack(side=TOP, expand=1, fill=BOTH)
        frame3.pack_propagate(False)

        self.figure2 = Figure(figsize=(10, 10), dpi=100)
        self.figure_canvas2 = FigureCanvasTkAgg(self.figure2, frame3)
        self.figure_canvas2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.plt2 = self.figure2.add_subplot(1,1,1)
        d = [(f"2024-{m}-01", f"2024-{m}-31") for m in ['02', '03', '04', '05', '06', '07', '08', '09', '10']]
        xx = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
        yy = [sqlitedb.get_month_category_sum('products', el[0], el[1])[0] for el in d]
        self.plt2.bar(xx, yy)

        frame4 = ttk.Frame(main_frame2, padding=10, borderwidth=1, relief=GROOVE)
        frame4.pack(side=BOTTOM, expand=0, fill=BOTH)
        frame4.config(height=100)
        frame4.pack_propagate(False)



        button4 = ttk.Button(master=frame4, text="Вклады",command=self._change)
        button4.pack(anchor=CENTER, expand=0)




        main_frame1.pack(side=LEFT, expand=1, fill=BOTH)
        main_frame1.pack_propagate(False)

        main_frame2.pack(side=RIGHT, expand=1, fill=BOTH)
        main_frame2.pack_propagate(False)










    def _change(self):
        print(1)
        self.figure1.clear()
        self.figure_canvas1.draw()
        self.plt2 = self.figure1.add_subplot(1, 1, 1)
        labels = ["Вклады", 'Долги', 'Накопительные счета', "Наличные", "Карты", "Инвестиции"]
        sizes = [1500000, 75000, 4000000, 1000, 500000, 0]

        self.plt2.pie(sizes, labels=labels, autopct="%1.1f%%")
        self.figure_canvas1.draw()


    def _update(self):
            pass
