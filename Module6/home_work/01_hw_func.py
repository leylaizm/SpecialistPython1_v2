# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
     b = ticket_number
    res = 'Счастливый'
    res1 = 'Не счастливый'
    if (b // 100000 % 10) + b // 10000 % 10 + b // 1000 % 10 == b // 100 % 10 + b // 10 % 10 + b // 1 % 10:
        return res
    else:
        return res1


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
