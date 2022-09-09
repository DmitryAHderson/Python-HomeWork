# Русские буквы оцениваются так:

points = {
    'АВЕИНОРСТAEIOULNSTR': 1,
    'ДКЛМПУDG': 2,
    'БГЁЬЯBCMP': 3,
    'ЙЫFHVWY': 4,
    'ЖЗХЦЧK': 5,
    'ШЭЮJX': 8,
    'ФЩЪQZ': 10
}

word = input('Введите слово: \n').upper()
points_counter = 0
for letter in word:
    for key in points.keys():
        if letter in key:
            points_counter += points[key]
            continue

print(points_counter)
