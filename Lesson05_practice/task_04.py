
# 1. Создать функцию, которая принемает (параметр) - число
# 2. Проверяет является ли число положительным либо отрицательным (if-else)
# 3. Выводит в консоль (print) сообщение положительное число или отрицательное число
# 4. Пользователь вводит с консоли число (input) и сохраняет его в перемнную
# 5. Программа вызывает (call) ранее созданную функцию,
# и передает полученное в п.4 число (аргумент)


def check_user_number(number):
    if number >= 0:
        print(f"\033[93mNumber {number} is \033[35mpositive\033[0m")
    else:
        print(f"\033[93mNumber {number} is \033[35mnegative\033[0m")


user_number = float(
    input("\033[31mEnter you number: \033[0m"))

check_user_number(user_number)
