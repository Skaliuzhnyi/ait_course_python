
import random

start = 10
end = 99
quantity = 10
random_list = [random.randint(start, end) for _ in range(quantity)]
print(random_list)


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


bubble_sort(random_list)
print(random_list)