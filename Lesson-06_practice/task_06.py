# def tax_calculation(salary_size):
#   amount = 1000
#   if salary_size < amount:
#       return "Налога нет!"
#   else:
#       new_tax = (salary_size - amount) * 19 / 100
#       return f"Ваш налог составляет: {new_tax}"


# my_salary = float(input("Введите размер вашей зарплаты: "))
# result = tax_calculation(my_salary)
# print(result)


def tax_calculation(salary_size):
    amount = 1000
    new_tax = (salary_size - amount) * 0.19

    return "Налога нет!" if salary_size < amount else f"Ваш налог составляет: {new_tax}$"


my_salary = float(input("Введите размер вашей зарплаты: "))
result = tax_calculation(my_salary)
print(result)
