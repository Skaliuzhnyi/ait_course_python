# Пользователь вводит с консоли (input), програма проверяет число (if-else)
# и печатаете в консоль (print) сообщение положительное число или отрицательное

def check_number():
    number = float(input("Enter you number: "))

    if number >= 0:
        print(f"Number {number} is positive")
    else:
        print(f"Number {number} is negative")


check_number()
