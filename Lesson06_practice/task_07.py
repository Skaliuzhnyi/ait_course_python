def tax_ukrain(salary):
    result = 0
    if salary > 1000:
      result = (salary - 1000) * 0.19
    return result
  
def salery_netto(salary):
    return salary - tax_ukrain(my_salary)
    

my_salary = float(input("Введите размер вашей зарплаты: "))
result = salery_netto(my_salary)
print(result)
