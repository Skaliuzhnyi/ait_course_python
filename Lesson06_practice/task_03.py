# 1. Создать функцию принимающую два параметра: имя пользователя и пароль
# Внутри функции сделать проверку: если (if) имя пользователя admin и (and) пароль admin,
# то вернуть текст: Доступ разрешен, иначе вернуть текст: Доступ запрещен
# 2. Попросить пользователя ввести с консоли свое имя, потом пароль
# 3. Вызвать функцию с введенными данными и результат сохранить в переменную
# 4. Распечатать значение переменной в консоли


def check_admin(name, password):
  
    # if name == "admin" and password == "admin":
    #     return "\033[32mAccess granted\033[0m"
    # else:
    #     return "\033[31mAccess denied\033[0m"
    
    return f"\033[32mAccess granted!\033[0m" if name == "admin" and password == "admin" else f"\033[31mAccess denied!\033[0m"


input_user_name = input(f"\033[35mEnter your name: \033[0m")
input_user_pass = input(f"\033[35mEnter your password: \033[0m")

result = check_admin(input_user_name, input_user_pass)
print(result)
