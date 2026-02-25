# Реализовать функцию selection_sort, которая принимает список
# и сортирует его с помощью алгоритма сортировки выбором.
# Сгенерировать список случайных чисел для тестирования
# Проверить работу функции selection_sort на сгенерированном списке

import random

start = 0
end = 89
quantity = 15
random_list = [random.randint(start, end) for _ in range(quantity)]


def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


print("Cгенерированный список:", random_list)
selection_sort(random_list)
print(f"Отсортированный список: {random_list}")
