# print('Упражнение 15')
# my_list = []
# i = 1
# print('Введите 3 целых числа: ')
# while i <= 3:
#     value = int(input())
#     my_list.append(value)
#     i += 1
# print('До сортировки', '\n', my_list)
# print('Min', '\n', min(my_list))
# print('Max', '\n', max(my_list))
# print('Оставшееся число', '\n', sum(my_list) - (max(my_list) + min(my_list)))
# print('*' * 30)
#
# print('Упражнение 16')
# bread = 3.49    # Стоимость свежего хлеба
# yesterday_bread = bread-(bread*0.6)     # Стоимость вчерашнего хлеба
# print('Введите количество вчерашнего хлеба: ')
# quantity_bread = int(input())    # Количество введеного хлеба
# sum_bread=quantity_bread * yesterday_bread
# print(f'Стоимость свежего: {bread} \n',
#       f'Вчерашнего: {"%.2f" % yesterday_bread}\n',
#       f'Общая стоимость вчерашнего {"%.2f" % sum_bread}\n')
# print('*' * 30)

# print('Упражнение 21')
#
# prise = 15  # Базовый тариф
# call_center = 0.44  # 911
#
# print('Введите количество минут и смс, \n '
#       'которые вы использовали \n')
# minutes = int(input('Минут: '))
# sms = int(input('СМС: '))
# if minutes <= 50 and sms <= 50:
#     basic_rate = prise + call_center + ((prise + call_center) * 0.05)  # Базовый тариф с налогом и кол.центром
#     print(f'Базовый тариф составляет: {prise} $')
#     print(f'Сумма в 911: {call_center} $')
#     print('Налог составит', "%.2f" % ((prise + call_center) * 0.05), '$')
#     print('Общая стоимость тарифа:', "%.2f" % basic_rate, '$')
# elif minutes > 50 and sms <= 50:
#     add_min = 0.25
#     add_sms = 0.15
#     min_not_rate = minutes - 50
#     add_min_prise = min_not_rate * add_min
#     full_prise = prise + call_center + add_min_prise + ((prise + call_center + add_min_prise) * 0.05)
#     # print("%.2f" % full_prise)
#     print(f'Базовый тариф составляет: {prise} $')
#     print(f'Стоимость доп.минуты = {add_min},\n доп.смс = {add_sms}')
#     print(f'Сумма в 911: {call_center} $')
#     print('Налог составит', "%.2f" % ((prise + call_center + add_min_prise) * 0.05), '$')
#     print(f'Доп минуты = {min_not_rate}, составят сумму', "%.2f" % add_min_prise, '$')
#     print('Полная цена составит: ', "%.2f" % full_prise, '$')
# elif minutes <= 50 and sms > 50:
#     add_min = 0.25
#     add_sms = 0.15
#     sms_not_rate = sms - 50
#     add_sms_prise = sms_not_rate * add_sms
#     full_prise = prise + call_center + add_sms_prise + ((prise + call_center + add_sms_prise) * 0.05)
#     # print("%.2f" % full_prise)
#     print(f'Базовый тариф составляет: {prise} $')
#     print(f'Стоимость доп.минуты = {add_min},\n доп.смс = {add_sms}')
#     print(f'Сумма в 911: {call_center} $')
#     print('Налог составит', "%.2f" % ((prise + call_center + add_sms_prise) * 0.05), '$')
#     print(f'Доп смс = {sms_not_rate}, составят сумму', "%.2f" % add_sms_prise, '$')
#     print('Полная цена составит: ', "%.2f" % full_prise, '$')
# else:
#     add_min = 0.25
#     add_sms = 0.15
#     sms_not_rate = sms - 50
#     min_not_rate = minutes - 50
#     add_min_prise = min_not_rate * add_min
#     add_sms_prise = sms_not_rate * add_sms
#     full_prise = prise + call_center + add_sms_prise + add_min_prise + \
#                  ((prise + call_center + add_sms_prise + add_min_prise) * 0.05)
#     # print("%.2f" % full_prise)
#     print(f'Базовый тариф составляет: {prise} $')
#     print(f'Стоимость доп.минуты = {add_min},\n доп.смс = {add_sms}')
#     print(f'Сумма в 911: {call_center} $')
#     print('Налог составит', "%.2f" % ((prise + call_center + add_sms_prise) * 0.05), '$')
#     print(f'Доп минуты = {min_not_rate}, составят сумму', "%.2f" % add_min_prise, '$')
#     print(f'Доп смс = {sms_not_rate}, составят сумму', "%.2f" % add_sms_prise, '$')
#     print('Полная цена составит: ', "%.2f" % full_prise, '$')
# print('*' * 30)

# print('Упражнение 22')
# year = int(input('Введите год: \n'))
# if year % 4 == 0 or ear % 400 == 0:
#     print('Этот год високосный!')
# else:
#     print('Этот год НЕ високосный!')
# print('*' * 30)

print('Упражнение 24')
string = input('Введите номерной знак: ')
print(string.upper())
# print(len([i for i in string if i.isdigit()]))
# print(len([i for i in string if i.isalpha()]))

d = {'Буквы': 0, 'Цифры': 0}
for i in string:
    if i.isalpha():  # Подсчет количества букв
        d['Буквы'] += 1
    elif i.isdigit():  # Подсчет количества цифр
        d['Цифры'] += 1

print(d['Цифры'], 'цифры', d['Буквы'], 'буквы!')

if d['Буквы'] == 3 and d['Цифры'] == 3:
    print('У вас старый формат номеров')
elif d['Цифры'] == 4 and d['Буквы'] == 3:
    print('У вас новый формат номеров')
else:
    print('Ошибка ввода')
