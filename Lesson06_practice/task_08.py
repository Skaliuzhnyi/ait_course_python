# Есть четыре команды работающие понедельно (вахтовым методом).
# Тимлиды: John, Peter, Mary, Ann.
# Комманда Джона работает в 1,5,9... и т. д. недели. Питера: 2,6,10... недели.
# Мэри: 3,7,11... недели. Анна: 4,8,12... недели
# В году недель 52
# 1. Написать функцию принимающую номер недели и возвращающую имя тимлида
# команда которого работает на соответствующей неделе.
# Если номер недели некоректный вернуть сообщение с ошибкой
# 2. Попросить пользователя ввести с консоли номер недели и сохранить его в переменную
# 3. Вызвать функцию с введенными данными и результат сохранить в переменную
# 4. Распечатать значение переменной в консоли

# def check_team(week):
#     team_John = 'John'
#     team_Peter = 'Peter'
#     team_Mary = 'Mary'
#     team_Ann = 'Ann'

#     weeks1 = list(range(1, 53, 4))
#     weeks2 = list(range(2, 53, 4))
#     weeks3 = list(range(3, 53, 4))
#     weeks4 = list(range(4, 53, 4))

#     if week in weeks1:
#         return team_John
#     elif week in weeks2:
#         return team_Peter
#     elif week in weeks3:
#         return team_Mary
#     elif week in weeks4:
#         return team_Ann
#     else:
#         return "Error"


# week_number = int(input("Введите номер недели: "))
# result = check_team(week_number)
# print(
#     f"Имя тимлида команда которого работает на соответствующей неделе - {result}" if result != "Error" else " Вы ввели не корректное значение недели!")

def check_team(week):

    if week > 52 or week < 1:
        return "Error"
    if week % 4 == 1:
        return "John"
    if week % 4 == 2:
        return "Peter"
    if week % 4 == 3:
        return "Mary"
    return "Ann"


week_number = int(input("Введите номер недели: "))
result = check_team(week_number)
print(
    f"Имя тимлида команда которого работает на соответствующей неделе - {result}" if result != "Error" else " Вы ввели не корректное значение недели!")
