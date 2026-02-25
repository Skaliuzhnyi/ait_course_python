
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


def binary_search(lst, value):
    l = 0
    r = len(lst) - 1
    while l <= r:
        middle = (l + r) // 2
        if lst[middle] == value:
            return middle
        elif lst[middle] < value:
            l = middle + 1
        else:
            r = middle - 1
    return -l - 1


index = binary_search(random_list, 50)
print(f'Index of 50: {index}')
index = binary_search(random_list, 71)
print(f'Index of 71: {index}')
index = binary_search(random_list, 99)
print(f'Index of 99: {index}')
index = binary_search(random_list, random_list[7])
print(f'Index of {random_list[7]}: {index}')



def bubbling(lst):
    flag = False
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            flag = True
    return flag

def bubble_sort1(lst):
    while bubbling(lst):