import random

start = 10
end = 99
quantity = 10
random_lst = []
for _ in range(quantity):
    rnd = random.randint(start, end)
    random_lst.append(rnd)

print(random_lst)
sorted_list = sorted(random_lst)
print(sorted_list)

random_lst = [random.randint(start, end) for _ in range(quantity)]
print(random_lst)
