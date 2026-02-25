# Employee: id, name, salary

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def calc_tax(self):
        tax = 0
        if self.salary > 1000:
            tax = (self.salary - 1000) * 0.19
        return tax

    def salary_netto(self):
        return self.salary - self.calc_tax()

    def __str__(self):
        return f'Id: \033[32m{self.id}\033[0m, Name: \033[32m{self.salary}\033[0m, Netto salary: \033[32m{self.salary_netto():.2f}\033[0m'


employee_1 = Employee(1000, 'Jon', 5400)
employee_2 = Employee(1001, 'Anton', 900)
employee_3 = Employee(1000, 'Ivan', 10200)

print(f'\033[36mEmployees taxes: \033[0m')
print(employee_1.calc_tax())
print(employee_2.calc_tax())
print(employee_3.calc_tax())

print('-' * 100)

print(f'\033[36mEmployees salary netto: \033[0m')
print(employee_1.salary_netto())
print(employee_2.salary_netto())
print(employee_3.salary_netto())

print('-' * 100)

employees_list = [employee_1, employee_2, employee_3]
print(f"\033[32mEmployees salary netto:\033[0m")
for employee in employees_list:
    print(
        f"   \033[36m{employee.name}'s:\033[0m {employee.salary_netto()}")

print('-' * 100)
print(f"\033[32mTotal netto salary of all employees:\033[0m {sum(employee.salary_netto() for employee in employees_list)}")
total_salary = 0
for employee in employees_list:
    total_salary += employee.salary_netto()
print("Total salary: ",total_salary) 
print("Total salary netto: ", total_salary) 
print("Average salary: ", round(total_salary / len(employees_list), 2))
