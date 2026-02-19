# Создать функцию, которая принимает число (параметр) и возвращает True,
# если число счастливое, а иначе возвращает False
# Число считается счастливым, если сумма цифр стоящих на четных позициях
# равна сумме цифр стоящих на нечетных позициях. Например число 1738649
# 1 + 3 + 6 + 9 == 7 + 8 + 4 => 19 == 19 - счастливое
# Вызвать функцию дважды: для счастливого и несчастливого чисел
# Если получаем True печатаем Lucky иначе печатаем Unlucky

def lucky_number(n):
    sum_even = 0
    sum_odd = 0
    pos = 1
    while n != 0:
        digit = n % 10
        if pos % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit
        n = n // 10
        pos += 1
    return sum_even == sum_odd


def lucky_number1(n):
    sum_even = 0
    sum_odd = 0
    while n != 0:
        digit = n % 10
        sum_even += digit
        n = n // 10
        digit = n % 10
        sum_odd += digit
        n = n // 10
    return sum_even == sum_odd

def lucky_number2(n):
    # Homework: Разобраться какой принцип лежит в основе этого алгоритма
    sum = 0
    while n != 0:
        sum = n % 10 - sum
        n = n // 10
    return sum == 0


print('Lucky' if lucky_number2(1738649) else 'Unlucky')
print('Lucky' if lucky_number2(1738549) else 'Unlucky')
