import csv
from valid_data import *


def acc_not_in_file(acc):
    try:
        with open('data.csv', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            s = list(reader)[1:]
        q = list(filter(lambda x: x, s))  # выкинем пустые строки
        num_acc = list(map(lambda x: x[0], q))
        return acc in num_acc
    except:
        print('File not exist')


def add_to_file(*list_of_data):
    try:
        with open('data.csv', mode='a', encoding='utf-8') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(list_of_data)
        return True
    except:
        print('File not exist')


def rewrite():
    pass


'''    try:
        with open('data.csv', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            # reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
            s = list(reader)[1:]
        old_list = list(filter(lambda x: x, s))  # выкинем пустые строки
        new_list = []
        for el in old_list:
            print(el)
            a = el[8][1:-1]
            if a:
                list_income = a.split(', ')
                last_data = list_income[-1][1:-1]
                print(last_data)
                days = between_income(last_data, int(el[7]))
            # нужно ли новое начисление
            if ready_to_add(last_data, days):
                if el[0] == el[6]:  # доход зачисляется на тот же счет
                    new_date = date_open(el[3], int(el[4]))
                    new_list.append([el[0], el[1], float(el[2]) + float(el[6]), new_date, 0, 0, 0, el[0], True])
                    el[-1] = True
                else:  # доход зачисляется на другой счет
                    was_find = False
                    if new_list:  # если есть обработанные вклады
                        for new_el in new_list:
                            if new_el[0] == el[7]:  # номера совпали
                                if ready_to_add(new_el[3], int(new_el[4])):  # целевой счет закрыт
                                    new_el[2] = float(new_el[2]) + float(el[6])  # добавили сумму дохода к  счету
                                    # добавили завершенный счет к списку обработанных
                                    new_list.append([el[0], el[1], el[2], el[3], 0, 0, 0, el[7], True])
                                else:  # целевой счет работает
                                    new_el[6] = float(new_el[6]) + float(el[6])  # добавили сумму дохода к доходу
                                    # добавили завершенный счет к списку обработанных
                                    new_list.append([el[0], el[1], el[2], el[3], 0, 0, 0, el[7], True])
                                el[-1] = True
                                was_find = True
                                break
                    # среди обработанных не нашли
                    if not was_find:
                        for new_el in old_list:
                            if new_el[0] == el[7]:
                                # добавляем доход это счета к доходам целевого
                                new_el[6] = float(new_el[6]) + float(el[6])
                                # заносим в список обработанных
                                new_list.append([el[0], el[1], el[2], el[3], 0, 0, 0, el[7], True])
                                el[-1] = True
            # срок вклада не окончен
            else:
                new_list.append(el)
        with open('data.csv', mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            head = ['acc', 'owner', 'sum_in', 'data_in', 'days', 'rate', 'acc_arrive',
                    'period', 'dt_was_income', 'Finised']
            writer.writerow(head)
            for el in new_list:
                writer.writerow(el)
    except:
        print("oops")
'''

'''print(acc_not_in_file('4'))

a = ['2', 'wer', 200, '20.20.2023', 365, 10, 20, 1, False]
print(add_to_file(*a))'''
# rewrite()
