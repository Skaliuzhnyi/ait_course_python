# Пользователь вводит с консоли число (input), програма проверяет число (if-else)
# и печатаете в консоль (print) сообщение число четное или нечетное
# четное число если делится без остатка на 2, нечетное в протичном случаи (используйте %)

# entered_number = int(input("Enter you number: "))
# if entered_number % 2 == 0:
#     print(f"Number {entered_number} is even number")
# else:
#     print(f"Number {entered_number} is odd number")


def check_input_number():
    try:
        entered_number = input("Enter you number: ")
        number = int(entered_number)
        if number % 2 == 0:
            print(f"Number {number} is even number")
        else:
            print(f"Number {number} is odd number")

    except ValueError:
        print("\033[31mError: You must enter an integer!\033[0m")


# check_input_number()
