def max_val(user_list):
    i = 0

    max_value = user_list[0]  # Инициализируем max_value первым элементом списка
    while i < len(user_list):
        if user_list[i] > max_value:  # Если текущий элемент больше max_value
            max_value = user_list[i]  # Обновляем max_value
        i += 1  # Увеличиваем i на 1 в каждой итерации (i = i + 1)

    return max_value  # Возвращаем максимальное значение после завершения цикла


num_user_list = [1, 2, 3, 4, 5, 189, 0, -1]
max_num = max_val(num_user_list)
print(f"Максимальное значение в списке: {num_user_list} - ", max_num)  # Should print 4

print(max_val([10, 20, 5, 30, 25]))  # Should print 30
print(max_val([-5, -10, -3, -1, -7]))  # Should print -1


def min_val(user_list):
    i = 0

    min_value = user_list[0]  # Инициализируем min_value первым элементом списка
    while i < len(user_list):
        if user_list[i] < min_value:  # Если текущий элемент меньше min_value
            min_value = user_list[i]  # Обновляем min_value
        i += 1  # Увеличиваем i на 1 в каждой итерации (i = i + 1)  
    
    return min_value  # Возвращаем минимальное значение после завершения цикла

print(f"Минимальное значение в списке: {num_user_list} - ", min_val(num_user_list))  # Should print -1
print("Минимальное значение в списке:", min_val([10, 20, 5, 30, 25]))  # Should print 5
print("Минимальное значение в списке:", min_val([-5, -10, -3, -1, -7]))  # Should print -10


def get_max(lst):
    max_value = lst[0]  # Инициализируем max_value первым элементом списка
    for num in lst:
        if num > max_value:  # Если текущий элемент больше max_value
            max_value = num  # Обновляем max_value
    return max_value  # Возвращаем максимальное значение после завершения цикла
  
print(get_max(num_user_list))  # Should print 189
print(get_max([10, 20, 5, 30, 25]))  # Should print 30
print(get_max([-5, -10, -3, -1, -7]))  # Should print -1

def get_min(lst):
    min_value = lst[0]  # Инициализируем min_value первым элементом списка
    for num in lst:
        if num < min_value:  # Если текущий элемент меньше min_value
            min_value = num  # Обновляем min_value
    return min_value  # Возвращаем минимальное значение после завершения цикла

print(get_min(num_user_list))  # Should print -10
print(get_min([10, 20, 5, 30, 25]))  # Should print 5