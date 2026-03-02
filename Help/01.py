import random

start = 10
end = 99
quantity = 10
random_list = [random.randint(start, end) for _ in range(quantity)]
print(random_list)


def selection_sort(list):
    sorted_list = []

    for i in range(len(list)):
        sorted_list.append(min(list))
        list.remove(min(list))
        i += 1
        
    return sorted_list


result = selection_sort(random_list)
print(result)
