def print_list(list):
    i = 0
    while i < len(list):
        print(f"[{i}] = {list[i]}")
        i += 1


def print_list1(list):
    for i in range(len(list)):
        print(f"[{i}] = {list[i]}")


primes = [2, 3, 5, 7, 11, 13, 17, 19]
print_list1(primes)
