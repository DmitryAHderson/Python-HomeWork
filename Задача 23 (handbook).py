print('Введите дату: \n')
input_day = int(input('Число:\n'))
input_month = int(input('Месяц:\n'))
input_year = int(input('Год:\n'))
date = []
date.append(input_day)
date.append(input_month)
date.append(input_year)
print(date)

# Условия
if input_year % 4 == 0 or input_year % 400 == 0 and input_month == 2:
    print('Этот год високосный!')
    if input_day < 29:
        date.clear()
        input_day = input_day + 1
        date.append(input_day)
        date.append(input_month)
        date.append(input_year)
        print(date)
    elif input_day == 29:
        date.clear()
        input_day = 1
        input_month = input_month + 1
        date.append(input_day)
        date.append(input_month)
        date.append(input_year)
        print(date)
    else:
        print(f'Этот год високостный и в феврале нет {input_day} дня ')

if input_year % 100 != 0 and input_month == 2:
    print('Этот год НЕ високосный!')
    if input_month == 2 and input_day < 28:
        date.clear()
        input_day = input_day + 1
        date.append(input_day)
        date.append(input_month)
        date.append(input_year)
        print(date)
    elif input_month == 2 and input_day == 28:
        date.clear()
        input_day = 1
        input_month = input_month + 1
        date.append(input_day)
        date.append(input_month)
        date.append(input_year)
        print(date)
    else:
        print(f'Этот год НЕ високостный, в феврале нет {input_day} дня')

if input_month == 1 or input_month == 3 or input_month == 5 or input_month == 7 or input_month == 8 or input_month == 10:
    if input_day < 31:
        date.clear()
        input_day = input_day + 1
        date.append(input_day)
        date.append(input_month)
        date.append(input_year)
        print(date)
    elif input_day == 31:
        date.clear()
        input_day = 1
        input_month = input_month + 1
        date.append(input_day)
        date.append(input_month)
        date.append(input_year)
        print(date)
    else:
        print(f'В {input_month} месяце 31 день, а не {input_day} !')

if input_month == 4 or input_month == 6 or input_month == 9 or input_month == 11:
    if input_day < 30:
        date.clear()
        input_day = input_day + 1
        date.append(input_day)
        date.append(input_month)
        date.append(input_year)
        print(date)
    elif input_day == 30:
        date.clear()
        input_day = 1
        input_month = input_month + 1
        date.append(input_day)
        date.append(input_month)
        date.append(input_year)
        print(date)
    else:
        print(f'В {input_month} месяце 30 дней, а не {input_day} !')

if input_month == 12:
    if input_day < 31:
        date.clear()
        input_day = input_day + 1
        date.append(input_day)
        date.append(input_month)
        date.append(input_year)
        print(date)
    elif input_day == 31:
        date.clear()
        input_day = 1
        input_month = 1
        input_year = input_year + 1
        date.append(input_day)
        date.append(input_month)
        date.append(input_year)
        print(date)
    else:
        print(f'В {input_month} месяце 31 день, а не {input_day} !')
