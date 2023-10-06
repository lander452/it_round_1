import csv
from time import sleep
from valid_data import *
from add_info import *
from work_with_file import *


# приветствие
def hello_line(lan=True):
    if lan:
        a = '''Вас приветствует Марк, разработчик этой программы \n
              Для работы в программе используйте следующие команды: '''
    else:
        a = '''greetings from Mark, the developer of this program' \n
                To work in the program, use the following commands:'''
    print(a)


# стартовое меню
def start_line(lan=True):
    if lan:
        a = '''
                read - просмотреть текущие данные
                add - рассчитать сумму дохода по вкладу / добавить новые данные 
                exit - завершить работу
                '''
    else:
        a = '''
                read - view current data
                add - calculate the amount of income on the deposit / add new data
                exit - exit
                '''
    print(a)


# меню чтения из файла
def read_line(lan=True):
    if lan:
        a = '''введите команду:
                all - для просмотра всех данных
                account - для просмотра данных по номеру счета
                owner - для просмотра данных по владельцу
                active - для просмотра данных по активным вкладам
                passive - для просмотра данных по завершенным вкладам 
                menu - вернуться в главное меню'''
    else:
        a = '''input command:
                all - 
                account - 
                owner - 
                active - 
                passive -  
                menu - return to main menu'''
    print(a)


# нет такой команды в меню
def er(lan=True):
    if lan:
        a = 'Проверьте ввод - нет такой команды'
    else:
        a = 'Check the input - there is no such command'
    print(a)


# об окончании работы
def say_bue_bue(lan=True):
    if fl:
        a = "Программа завершила свою работу"
    else:
        a = "The work has ended"
    print(a)


# выбор языка управления
q = ''

while not (q == '1' or q == '2'):
    print("Выберите язык/ Select a language:")
    print('Введите '
          '1 (для выбора русского языка) '
          '2 (for english language)')
    q = input()
if q == '1':
    fl = True
else:
    fl = False

hello_line(fl)
start_line(fl)

command = input().lower()
while command != 'exit':
    # вернулись в основное меню
    if command == 'menu':
        start_line(fl)
    # будем читать из файла
    elif command == 'read':
        try:
            with open('data.csv', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                s = list(reader)[1:]
            for el in s:
                if el:
                    if fl:
                        print(f"Номер счета {el[0]}, владелец {el[1]}")
                        print(f"Счет открыт {el[3]} на дней {el[4]}")
                        print(f"На счету сумма {el[2]} под {el[5]}%")
                        print(f'Доход составит {el[6]}, будет внесен на счет {el[7]}')
                        if el[-1] == "True":
                            print('Срок действия вклада уже истек')
                        else:
                            print('Срок действия вклада еще не истек')

                    else:
                        print("You have entered the next information:")
                        print(f"Account number {el[0]}, owner {el[1]}")
                        print(f"Account opened {el[3]} for {el[4]}")
                        print(f"Amount {el[2]} entered under {el[5]}%")
                        print(f'Income amount {el[6]}, will be deposited into account {el[7]}')
                        if el[-1] == "True":
                            print('Account has expired')
                        else:
                            print('The account has not expired yet')
                    print("-" * 100)

        except:
            if fl:
                print("Файл с информацией был утерян. Попробуйте ввести ее заново в меню add")
            else:
                print('The file with the information was lost. Try to re-enter it in the add menu')

        start_line(fl)
    # будем писать в файл
    elif command == 'add':
        answer = main_count()
        if will_be_save():
            if answer:
                acc, owner, sum_in, data_in, days, rate, sum_in_first, sum_in_second, acc_arrive, period, dt_was_income, finished = answer
                if fl:
                    print("Вы ввели следующую информацию:")
                    print(f"Номер счета {acc}, владелец {owner}")
                    print(f"Счет открыт {data_in} на дней {days}")
                    print(f"Внесена сумма {sum_in} под {rate}%")

                else:
                    print("You have entered the next information:")
                    print(f"Account number {acc}, owner {owner}")
                    print(f"Account opened {data_in} for {days}")

                '''if ready_to_add(data_in, days):
                    if fl:
                        print("Вклад завершен, проценты будут начислены на целевой счет")
                    else:
                        print('Deposit completed, interest will be credited to the target account')'''
                if acc == acc_arrive:
                    sum_bonus = 0
                    finished = True
                    add_to_file(acc, owner, sum_in_first, data_in, days, rate, acc_arrive, period,
                                    dt_was_income, finished)
                else:
                    if acc_not_in_file(acc_arrive):
                        new_data = date_open_str(data_in, days)
                        if fl:
                            print(f"Создан новый счет {acc_arrive} на {owner}, дата открытия {new_data}")

                        else:
                            print(f"Created new account {acc_arrive} on {owner}, opening date {new_data}")
                        add_to_file(acc_arrive, owner, sum_in_second, new_data, 0, 0, acc_arrive, 0, None, False)
                    else:
                        rewrite()
                        if fl:
                            print("Все счета обработаны")
                        else:
                            print("All accounts have been processed")

        start_line(fl)
    # пользователь ввел ерунду
    else:
        er(fl)
        start_line(fl)
    command = input().lower()

say_bue_bue(fl)
sleep(5)
