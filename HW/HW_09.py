numbers_list = [10, 20, 30, 40, 50]

x = 30
y = 35

x_position = numbers_list.index(x)
numbers_list.insert(x_position + 1, y)
print(numbers_list)