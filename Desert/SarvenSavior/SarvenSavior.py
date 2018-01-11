# Массив - это список элементов.
# Этот массив - список имен твоих друзей.
friendNames = ['Joan', 'Ronan', 'Nikita', 'Augustus']

# Индекс массива начинается с 0, а не с 1!
friendIndex = 0

# Включи в цикл все имена в массиве.
# Функция len() возвращает длину списка.
while friendIndex < len(friendNames):
    # Используй квадратные скобки чтобы извлечь имя из массива.
    friendName = friendNames[friendIndex]

    # Прикажи другу идти домой.
    # Используй + для объединения двух строковых элементов.
    hero.say(friendName + ', go home!')

    # Увеличивай индекс, чтобы получить следующее имя из массива.
    friendIndex += 1
hero.moveXY(25, 30)
hero.buildXY('fence', 29, 30)
# Вернись и построй частокол, чтобы защититься от огров.