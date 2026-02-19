def print_even_numbers(number):
    print("\033[34mЧетные числа от 1 до", number, ":\033[0m")
    # for i in range(1, number + 1):
    #     if i % 2 == 0:
    #         print(i)
    
    i = 0
    while i <= number:
        if i % 2 == 0:
            print(i)
        i += 1 # Увеличиваем i на 1 в каждой итерации (i = i + 1)
    
number = int(input("Введите число: "))
print_even_numbers(number)
