lst = []
for num in range(10):
    lst.append(num * num)

print(lst)

lst_comp = [num * num for num in range(4, 20, 3)]
print(lst_comp)
