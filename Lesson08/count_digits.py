# Создать функцию принимающую (параметр) целое число,
# и возвращающую (return) колличество цифр в этом числе
# Например число 123 имеет 3 цифры, -67 - 2 цифры
# Проверить работу функции вызвав ее несколько раз с разными аргументами

def count_digits(number):
    # number = number if number >= 0 else -number
    number = abs(number)
    # if number == 0:
    #     return 1
    accum = 0
    while number != 0:
        accum += 1 # accum = accum + 1
        number //= 10 # number = number // 10
    return accum if accum != 0 else 1

res = count_digits(123)
print(f"count digits = {res}")
res = count_digits(-67)
print(f"count digits = {res}")
res = count_digits(5)
print(f"count digits = {res}")
res = count_digits(0)
print(f"count digits = {res}")
res = count_digits(2001)
print(f"count digits = {res}")