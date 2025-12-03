import sqlitedb

sqlitedb.database_init()
sqlitedb.make_expenses()
# sqlitedb.add_day_expenses("products", 1500, "23-11-25")

#
# sqlitedb.get_day_expenses('products', '23-11-25')
# sqlitedb.get_day_expenses('products', '24-11-25')
# sqlitedb.get_day_expenses('sport', '24-11-25')
# sqlitedb.get_total_category_expenses("sport")
# sqlitedb.get_total_category_expenses("products")
# sqlitedb.get_day_expenses(3)
# sqlitedb.show()

while(True):
    print("0 - EXIT\n1 - Ввод расхода\n2 - Вывод\n")
    T = int(input())

    if T == 0:
        print("EXIT")
        break

    if T == 1:
        print("Категория: ")
        category_name = str(input())
        print("Сумма: ")
        summa = int(input())
        print("Дата: (xx-xx-xx) ")
        data = str(input())

        sqlitedb.add_day_expenses(category_name, summa, data)

        print(category_name, summa, data)
        continue

    if T == 2:
        sqlitedb.show()
