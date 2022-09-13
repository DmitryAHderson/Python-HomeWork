print('Упражнение 35')
# BASE = 4
# PART = 140
# PART_PRICE = 0.25
#
#
# def taxi(distance):
#     if not isinstance(distance, (int, float)):
#         return 'Введите число'
#     # if type(distance) == int or type(distance) == float :
#     #     return 'Введите число'
#     if distance <= 0:
#         return f'{distance} должно быть больше 0!'
#     metres = (distance * 1000) / PART
#     sum = BASE + metres * PART_PRICE
#     return f'{sum}$'
#
#
# print(taxi(0.14))
# print(taxi(1))
# print(taxi(0))
# print(taxi(120))
# print(taxi(-10))
# print(taxi('0'))

# print('Упражнение 36')
# first_item = 10.95
# next_items = 2.95
#
#
# def delivery(position=int(input('Введите количество позиций в заказе: \n'))):
#     if position <= 0:
#         return f'{position} позиций,должно быть больше 0!'
#     if position == 1:
#         return (f'{first_item}$')
#
#     else:
#         full_prise = first_item + ((position - 1) * 2.95)
#         return (f'{full_prise}$')
#
#
# print(delivery())

print('Упражнение 41')

password = input('Введите пароль: ')


def goodPassword(password):
    digit = 0
    low_reg = 0  # Нижний регистр
    up_reg = 0  # Верхний регистр
    for symbol in password:
        if symbol.isdigit():
            digit = 1
        if symbol.isalpha():
            if symbol.islower():
                low_reg = 1
            else:
                up_reg = 1
    return len(password) >= 8 and digit and low_reg and up_reg


if goodPassword(password):
    print('Пароль надежный.')
else:
    print('Пароль ненадежный!')
