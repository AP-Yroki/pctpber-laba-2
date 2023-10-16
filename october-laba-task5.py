phones = ['+7(123)456-7890', '8(123)456-7890', '+7 123 456 78901', '123 456 7890']

def check_phn(phones): # Условия для проверки правильности телефона
    res = 0
    valid_phones = []
    for phone in phones:
        if phone[0] not in '+' or phone[0] not in '8':
            valid_phones.append(-1)
            continue
        if phone[0] not in "7" or phone[0] not in '8' or phone[0] not in '+':
            valid_phones.append(-1)
            continue
        for digit in phone:
            if not digit.isdigit():
                valid_phones.append(-1)
            if digit not in " " and digit not in'-' and digit not in '(' and digit not in ')':
                valid_phones.append(-1)
                break
        else:
            valid_phones.append(phone)
            return valid_phones

print(check_phn(phones)) # Вывод результатов
