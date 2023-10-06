from valid_data import *
from time import sleep

# account;owner;sum_in;data_in;days;rate;sum_bonus;account_arrive;arrived
fl = True


# проверка корректности ввода (не пустая строка, не содержит ;)
def check_to_valid(in_line):
    return True if (';' not in in_line and len(in_line)) else False


# проверка корректности введенной суммы
def check_to_valid_sum(in_sum):
    if check_to_valid(in_sum) and (',' not in in_sum):
        try:
            if float(in_sum) > 0:
                return True
            else:
                if fl:
                    print("Это должно быть положительное значение")
                else:
                    print('This must be a positive value')
                return False
        except:
            return False


# проверка корректности введенной даты
def check_to_valid_data(in_data):
    if check_to_valid(in_data) and ('.' in in_data):
        if len(in_data.split('.')) == 3:
            d, m, y = in_data.split('.')
            if d.isdigit() and int(d) < 32:  # дней не больше 31
                d = int(d)
            else:
                if fl:
                    print("В месяце не может быть столько дней")
                else:
                    print('Too much days in month')
                return False
            if m.isdigit() and int(m) < 13:  # месяцев не больше 12
                m = int(m)
                if (m == 2 and d > 29) or (d == 31 and m in [9, 4, 6, 11]):
                    if fl:
                        print("В этом месяце не может быть столько дней")
                    else:
                        print('Too much days in this month')
                    return False
            else:
                if fl:
                    print("В году только 12 месяцев")
                else:
                    print('No more 12 months, please')
                return False
            if y.isdigit() and (2000 <= int(y) < 2024):  # считаем корректной дату начала вклада не позже этого года
                y = int(y)
                # проверим, високосный или нет
                if not ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):  # не високосный
                    if d == 29 and m == 2:
                        if fl:
                            print("Этот год не високосный, попробуйте еще раз")
                        else:
                            print('This is not a leap year. Please, try again')
                        return False
            else:
                return False
        else:
            return False
        return True


def check_to_valid_days(in_days):
    if check_to_valid and in_days.isdigit():
        return True
    else:
        False


# получение суммы, срока и % ставки вклада
def get_sum_days_rate():
    days, rate, sum_inn = '', '', ''

    # получаем сумму вклада
    while not check_to_valid_sum(sum_inn):
        if fl:
            print('Введите сумму вклада. \n'
                  'Если это необходимо, то в качестве разделителя целой и дробной части используйте точку')
        else:
            print("Input size of deposit\n"
                  "Use the dot as the separator of the integer and fractional parts\n")
        sum_inn = input()
    sum_in = float(sum_inn)

    # получаем срок вклада
    while not check_to_valid_days(days):
        if fl:
            print('Введите срок вклада в ДНЯХ')
        else:
            print("Enter the deposit term in DAYS ")
        days = input()
    days = int(days)

    # получаем % ставку
    while not check_to_valid_sum(rate):
        if fl:
            print('Введите размер процентной ставки')
        else:
            print("Enter the interest rate")
        rate = input()
    rate = float(rate)
    return sum_in, days, rate


# получаем корректный счет
def get_acc():
    acc = ''
    while not check_to_valid(acc):
        if fl:
            print('Введите номер счета')
        else:
            print("Input number of account")
        acc = input()
    return acc


# сбор данных о вкладе
def get_owner_info():
    owner, data_in = '', ''
    # получаем владельца
    while not check_to_valid(owner):
        if fl:
            print('Введите владельца счета')
        else:
            print('Input owner of account')
        owner = input()

    # получаем дату начала вклада
    while not check_to_valid_data(data_in):
        if fl:
            print('Введите дату вклада в формате день.месяц.год \n'
                  'Год пишите полностью, например,  2023')
        else:
            print('Enter the deposit date in the format: day.month.year \n'
                  'Write full year, for example, 2023')
        data_in = input()
    acc = get_acc()
    acc_arrive = ''
    # выбор, куда начислять проценты
    while not (acc_arrive == '1' or acc_arrive == '0'):
        if fl:
            print("Если хотите зачислить доход на этот же счет, введите 0 \n"
                  "Иначе введите 1")
        else:
            print("If you want to credit income to the same account, enter 0 \n"
                  "Otherwise enter 1")
        acc_arrive = input()
    if acc_arrive == '0':
        acc_arrive = acc
    else:
        acc_arrive = acc
        while acc_arrive == acc:
            if fl:
                print('Номера счетов должны отличаться!')
            else:
                print('Account numbers must be different!')
            acc_arrive = get_acc()
    return owner, data_in, acc, acc_arrive


def get_period():
    p = ''
    while not (p == '1' or p == '2' or p == '3'):
        if fl:
            print('Выберите периодичность начисления процентов')
            print('Введите 1 - для начисления ежемесячно')
            print('Введите 2 - для начисления ежеквартально')
            print('Введите 3 - для начисления ежегодно')
        else:
            print('Choose the period of interest accrual')
            print('Input 1 - monthly')
            print('Input 2 - quarterly')
            print('Input 3 - annually')
        p = input()
    return int(p)


def main_count():
    # сбор первоначальных данных
    sum_in, days, rate = get_sum_days_rate()
    owner, data_in, acc, acc_arrive = get_owner_info()
    period = get_period()

    a = [int(x) for x in data_in.split('.')]
    days_between = between_income(data_in, period)  # дней до первого начисления
    # print(days_between)
    date_start = dt.date(a[2], a[1], a[0])
    data_end = date_start + dt.timedelta(days=days_between)  # дата первого начисления

    # print(data_end)
    sum_in_first, sum_in_first_now = sum_in, sum_in
    sum_in_second, sum_in_second_now = 0, 0
    dt_income = [data_end]

    while date_open(data_in, days) >= dt_income[-1]:
        # print(date_open(data_in, days), dt_income[-1])
        income = round((sum_in_first * rate * (days_between / 365)) / 100, 4)
        if acc != acc_arrive:  # доход зачисляется на другой счет
            sum_in_second += income
            if dt_income[-1] < dt.date.today():
                if fl:
                    print(f'Дата {dt_income[-1]}, начисление {income}')
                else:
                    print(f'Date {dt_income[-1]}, income {income}')
                sum_in_second_now += income
        else:  # % начисляются на тот же счет
            sum_in_first += income

            if dt_income[-1] < dt.date.today():
                if fl:
                    print(f'Дата {dt_income[-1]}, начисление {income}')
                else:
                    print(f'Date {dt_income[-1]}, income {income}')
                sum_in_first_now += income
        data_new = dt_income[-1] + dt.timedelta(days=days_between)

        dt_income.append(data_new)
    dt_was_in = list(filter(lambda x: x <= dt.date.today(), dt_income))
    dt_was_income = list(map(lambda x: str(x.day) + '. ' + str(x.month) + '.' + str(x.year), dt_was_in))
    #print(dt_was_income)
    # print(dt_income)
    # print(sum_in_first, sum_in_second, sum_in_first_now, sum_in_second_now)

    if fl:
        if acc != acc_arrive:
            print(f"Доход с {sum_in} за {days} дней по ставке {rate}% составит {sum_in_second}")
            print(f'Сейчас на доходном счету {sum_in_second_now}')
        else:
            print(f"Сумма на счету на конец периода в {days} дней по ставке {rate}% составит {sum_in_first}")
            print(f'Сейчас на счету {sum_in_first_now}')
    else:
        if acc != acc_arrive:
            print(f"Income from {sum_in} for {days} days at the rate {rate}% will be {sum_in_second}")
            print(f'Now in arrive account {sum_in_second_now}')
        else:
            print(
                f"The amount on the account at the end of the period of {days} days at a rate of {rate}% will be {sum_in_first}")
            print(f'Now in account {sum_in_first_now}')
    answer = [acc, owner, sum_in, data_in, days, rate, sum_in_first, sum_in_second, acc_arrive, period, dt_was_income,
              False]
    return answer


# сбор оставшейся информации для записи в файл
def will_be_save():
    ans = ''
    while not (ans == '1' or ans == '0'):
        if fl:
            print("Будем оформлять вклад? Если ДА, введите 1, иначе введите 0")
        else:
            print("Shall we save? If YES enter 1 else enter 0")
        ans = input()
    if ans == '1':
        return True
    else:
        return False


if __name__ == '__main__':
    main_count()
