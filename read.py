import openpyxl

def get_data(cat_num, cat_name):
    workbook = openpyxl.load_workbook("1.xlsx")
    sheet = workbook[str("Лист1")]

    content = []

    for i in range(2, 625):
        tmp = sheet.cell(row=i, column=1).value
        date = tmp.strftime('%d-%m-%y')

        tmp_sum = sheet.cell(row=i, column=cat_num).value
        if tmp_sum is None:
            tmp_sum = 0
        if isinstance(tmp_sum, str):
            b = tmp_sum[1:]
            bb = b.split('+')
            tmp_sum = sum([int(x) for x in bb])

        content.append((cat_name, tmp_sum, date))

    # print(content)
    return content

a = get_data(5, 'products')

print(a[0])