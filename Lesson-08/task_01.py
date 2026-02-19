def search(list, value):
    for i in list:
        if i == value:
            return True
    return False

my_list = [1, 2, 3, 4, 5]
print(search(my_list, 3))  # Should print True
print(search(my_list, 6))  # Should print False

print(90 in my_list)  # Should print False

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Should print True
print("grape" in fruits)   # Should print False