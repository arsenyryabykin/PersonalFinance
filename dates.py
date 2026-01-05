import calendar
from datetime import date, timedelta, datetime
import locale


locale.setlocale(locale.LC_ALL, "")
# num_days = calendar.monthrange(2024, 2)[-1]


def get_last_30_days() -> list:
    # TODO: Исправить конкретные даты после загрузки данных
    '''
    Создает список последних 30 дней от текущей даты в формате "07 Октябрь 2025 (Вт)"
    
    :return: Description
    :rtype: list
    '''
    day = date.today() - timedelta(60)
    last_month = [(day - timedelta(i)).strftime("%d %B %Y (%a)") for i in range(0, 31)]
    return last_month

def get_last_30_days_unformat() -> list:
    # TODO: Исправить конкретные даты после загрузки данных
    '''
    Создает список последних 30 дней от текущей даты в неформатированном виде datetime.date

    :return: Description
    :rtype: list
    '''
    day = date.today() - timedelta(60)
    last_month = [(day - timedelta(i)) for i in range(0, 31)]
    return last_month


a = get_last_30_days_unformat()
print(a)


# b = get_last_30_days()
# print(b)
# dt = datetime.strptime(a, "%d %B %Y (%a)").date()
# print(dt)