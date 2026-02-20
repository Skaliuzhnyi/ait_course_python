user_num = int(input("Enter a number: "))

if user_num == 0:
    pass
elif user_num == 1:
    print(0)
else:
    fib = [0, 1]
    while len(fib) < user_num:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
    print(fib)