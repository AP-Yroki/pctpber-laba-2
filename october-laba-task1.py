ref = [ ['Александр', 'Анастасия'], ['Смирнов',   'Иванова'] ]
def list_reorder(ref):
    names = ref[0]
    families = ref[1]
    result = [] # создание переменной для результата
    for i in range(len(names)): # Создал цикл, где к именам добавляются фамилии
        result.append([names[i], families[i]])
    return result # Возврат результата

print(list_reorder(ref)) # Вызов функции