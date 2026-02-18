# Создать функцию, которая принимает (параметр) список и возвращает сумму его
# нечетных элементов. Создать список из произвольных чисел.
# Вызвать функцию, передав этот список в качестве аргумента.
# Результат сохранить в переменную, которую надо вывести в консоль

def odds_sum_list(list):
    sum = 0
    for num in list:
        if num % 2 != 0:
            sum += num
    return sum

list = [1, 9, 2, 8, 3, 7, 4, 6, 5, 0]
res = odds_sum_list(list)
print(f"sum of digits odds = {res}")
primes = [2, 3, 5, 7, 11, 13, 17, 19]
res = odds_sum_list(primes)
print(f"sum of primes odds = {res}")