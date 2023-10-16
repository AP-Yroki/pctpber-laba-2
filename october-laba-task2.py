nums = [1, 2, 3, 3, 4, 5, 6, 6]

def del_rep(nums): # Функция которая сортирует, и возвращает список без дубликатов
    nums.sort() # Сортировка списка
    new_list = [] # Создание нового списка для результатов
    for num in nums: # Перебор списка
        if num not in new_list: # Удаление дубликатов
            new_list.append(num)
    return new_list # Возврат результата

print(del_rep(nums)) # Вызов функции