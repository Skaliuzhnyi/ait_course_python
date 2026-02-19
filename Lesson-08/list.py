list1 = [20, 30, 15, 10, 20]
print(list1)
print(f"list1[2] = {list1[2]}")
# print(f"list1[5] = {list1[5]}") # Error
print(f"list1 length = {len(list1)}")
print(f"length of string 'Hello world' = {len('Hello world')}")
number = 1239857
print(f"count digits in {number} = {len(str(number))}")
list1[2] = 45
print(f"list1[2] = {list1[2]}")
i = 4
print(f"list1[{i}] = {list1[i]}")
i = 0
print(f"list1[{i}] = {list1[i]}")
i = int(input("Enter index: "))
input_number = int(input(f"Enter new value for index = {i}: "))
list1[i] = input_number
print(f"list1[{i}] = {list1[i]}")
print(list1)