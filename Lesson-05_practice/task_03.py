
# Пользователь вводит с консоли число (input) - свою часовую ставку оплаты (wage)
# Потом вводит в консоль сколько часов он отработал за месяц
# Программа рассчитывает и выводит в консоль (print) зарплату пользователя

wage = float(input("Enter your hourly rate of pay: "))
hours_worked = float(
    input("Enter the number of hours you worked: "))

salary = wage * hours_worked

print(f"Your salary for this month was - {salary}$")
