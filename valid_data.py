import datetime as dt


# проверка, закончилось ли действие вклада на сегодняшний момент
def ready_to_add(start_date, period):
    a = [int(x) for x in start_date.split('.')]
    date_start = dt.date(a[2], a[1], a[0])
    delta_time = dt.timedelta(days=period)
    data_end = date_start + delta_time
    if data_end <= dt.datetime.now().date():
        return True
    else:
        return False


# расчет когда окончание действия вклада, строка
def date_open_str(start_date, period):
    a = [int(x) for x in start_date.split('.')]
    date_start = dt.date(a[2], a[1], a[0])
    delta_time = dt.timedelta(days=period)
    data_end = str(date_start + delta_time).split('-')
    ans = str(data_end[2]) + '.' + str(data_end[1]) + '.' + str(data_end[0])
    return ans

# расчет когда окончание действия вклада, datatime
def date_open(start_date, period):
    if type(start_date) == str:
        a = [int(x) for x in start_date.split('.')]
        date_start = dt.date(a[2], a[1], a[0])
    else:
        date_start = start_date
    delta_time = dt.timedelta(days=period)
    data_end = date_start + delta_time
    return data_end


# расчет сколько дней между начислениями
def between_income(start_date, period):
    if type(start_date) == str:
        a = [int(x) for x in start_date.split('.')]
        date_start = dt.date(a[2], a[1], a[0])
    else:
        a = [int(x) for x in str(start_date).split('-')]
        date_start = dt.date(a[0], a[1], a[2])
    #print(date_start)
    if period == 1:
        if a[1] < 12:
            a[1] += 1
        else:
            a[1] = 1
            a[2] += 1
    elif period == 2:
        if a[1] <= 9:
            a[1] += 3
        else:
            a[1] = (a[1] + 3) % 12
            a[2] += 1
    else:
        a[2] += 1
    if a[0] == 31 and a[1] in [9, 4, 6, 11]:
        a[0] = 1
        a[1] += 1
    elif a[0] > 29 and a[1] == 2:
        a[0] -= 28
        a[1] = 3
    if type(start_date) == str:
        date_end = dt.date(a[2], a[1], a[0])
    else:
        date_end = dt.date(a[0], a[1], a[2])
    delta_time = (date_end - date_start).days
    return delta_time

