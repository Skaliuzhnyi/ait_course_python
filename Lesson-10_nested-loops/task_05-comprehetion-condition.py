import random

start = 10
end = 99
quantity = 10

random_lst = [random.randint(start, end) for _ in range(quantity)]
print(f"\033[31mRandom numbers of 'random_lst': \033[0m{random_lst}")

print('-' * 100)

# Только не четные числа
odd_lst = [random.randint(start, end) for _ in range(quantity) if _ % 2 != 0]
print(f"\033[31mOdd numbers of 'odd_lst': \033[0m{odd_lst}")

print('-' * 100)

# Только четные числа из random_lst
even_lst = [a for a in random_lst if a % 2 == 0]
print(f"\033[31mEven numbers of 'random_lst': \033[0m{even_lst}")

print('-' * 100)

pass_exam = [exam for exam in random_lst if exam >= 80]
print(f"\033[31mPassed exam numbers of 'pass_exam': \033[0m{pass_exam}")

print('-' * 100)