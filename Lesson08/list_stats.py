list = [1, 9, 2, 8, 3, 7, 4, 6, 5, 0]


def sum_list(list):
    sum = 0
    for num in list:
        sum += num
    return sum


def avg_in_list(list):
    return sum_list(list) / len(list)


res = sum_list(list)
print(f"sum of digits = {res}")
res = avg_in_list(list)
print(f"average of digits = {res}")
primes = [2, 3, 5, 7, 11, 13, 17, 19]
res = sum_list(primes)
print(f"sum of primes = {res}")
res = avg_in_list(primes)
print(f"average of primes = {res}")
