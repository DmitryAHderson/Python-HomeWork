import random

name_team = input('Введите имя / название команды : ')
enemy_team = [" 'Супер'", " 'Кока-Колы'", "'Мы лучшие!'"]
print(
    f'Отлично ! {name_team.capitalize()},против вас играет команда {random.choice(enemy_team)}, давайте начнем!')  # capitalize -первая буква заглаваная, остальные маленькие
counter = 0
enemy_counter = 0
print()
print('Вопрос 1')
questions = {"Как называется самая известная смотровая площадка Москвы?\n": 'воробьевы горы'}

for question, value in questions.items():
    print(question)
    print(' 1:воробьевы горы\n', '2:вднх\n', '3:красная площадь\n')
    answer = str(input('Ваш ответ:'))
    if answer == value:
        print('Правильный ответ!')
        counter += 1
    else:
        print('Ответ не верный!')

enemy_questions = ["воробьевы горы", "вднх", "красная площадь"]
enemy_answer = random.choice(enemy_questions)
if enemy_answer == "воробьевы горы":
    enemy_counter += 1

print(f'Ваш ответ :{answer}\nОтвет соперника: {enemy_answer}')
print(f'Ваши балы: {counter}\nБалы соперника: {enemy_counter}')
print()
print('Вопрос 2')
questions = {"Известный код из Матрици на самом деле обозначает....\n": 'рецепт суши'}

for question, value in questions.items():
    print(question)
    print(' 1:ссылка на офф.сайт фильма\n', '2:рецепт суши\n', '3:рандомный код\n')
    answer = str(input('Ваш ответ:'))
    if answer == value:
        print('Правильный ответ!')
        counter += 1
        print(f'Ваши балы {counter}')
    else:
        print('Ответ не верный!')

enemy_questions = ["ссылка на офф.сайт фильма", "рецепт суши", "рандомный код"]
enemy_answer = random.choice(enemy_questions)
if enemy_answer == "рецепт суши":
    enemy_counter += 1

print(f'Ваш ответ :{answer}\nОтвет соперника: {enemy_answer}')
print(f'Ваши балы: {counter}\nБалы соперника: {enemy_counter}')
print()
print('Вопрос 3')
questions = {"Что в море является ориентиром для моряка": 'полярная звезда'}

for question, value in questions.items():
    print(question)
    print(' 1:полярная звезда\n', '2:маяк\n', '3:большая медведица\n', '4:другие моряки')
    answer = str(input('Ваш ответ:'))
    if answer == value:
        print('Правильный ответ!')
        counter += 1
        print(f'Ваши балы {counter}')
    else:
        print('Ответ не верный!')

enemy_questions = ["полярная звезда", "маяк", "большая медведица", "другие моряки"]
enemy_answer = random.choice(enemy_questions)
if enemy_answer == "полярная звезда":
    enemy_counter += 1

print(f'Ваш ответ :{answer}\nОтвет соперника: {enemy_answer}')
print(f'Ваши балы: {counter}\nБалы соперника: {enemy_counter}')


if counter > enemy_counter:
    print('Вы победили в игре!')
elif counter == enemy_counter:
    print('Ничья, победила дружба!')
else:
    print('Вы проиграли команде соперника!')