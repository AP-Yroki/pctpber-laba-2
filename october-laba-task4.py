temp = int(input('Введите температуру: ')) # Получение температуры

def temp_cat(temp): # Функция которая возвращает номер категории

    temp_list = { # Создание словаря с ключами для категории
        0: '# Холодно',
        1: '# Прохладно',
        2: '# Зябко',
        3: '# Тепло',
        4: '# Жарко',
    }
    if temp < -20: # Условии проверяющие какой каталог на выводить
        return (f'0 {temp_list[0]}')
    elif temp < 0:
        return (f'1 {temp_list[1]}')
    elif temp < 15:
        return (f'2 {temp_list[2]}')
    elif temp < 25:
        return (f'3 {temp_list[3]}')
    elif temp > 25:
        return (f'4 {temp_list[4]}')

print(temp_cat(temp)) # Вывод результатов

