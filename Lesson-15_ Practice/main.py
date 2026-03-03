from company.repository.company import Company
from company.model.manager import Manager
from company.model.wage_employee import WageEmployee
from company.model.sales_manager import SalesManager

company = Company('ABC Company')
company_2 = Company('KGK Implement')

manager_1 = Manager(1000, 'John', 'Doe', 160, 10_000, 20)
manager_2 = Manager(1001, 'Ivan', 'Dre', 160, 7_300, 20)
we_1 = WageEmployee(2000, 'Jane', 'Smith', 16, 25)
wg_2 = WageEmployee(2001, 'Ann', 'Smith', 18, 22)
sm_1 = SalesManager(3000, 'Peter', 'Parker', 160, 10_000, 0.1)
sm_2 = SalesManager(3001, 'Andrey', 'Potrtnov', 80, 60_000, 0.13)

company.add_emploee(manager_1)
company.add_emploee(manager_1)
company.add_emploee(manager_2)
company.add_emploee(we_1)
company.add_emploee(sm_1)
company.add_emploee(sm_2)
company.print_employees()

print('-' * 100)

print("Total numbers of employees:", company.quantity())

print('-' * 100)

lost_employee_1 = company.find_emploee(1000)
print(lost_employee_1)

print('-' * 100)

lost_employee_2 = company.find_emploee(1030)
print(lost_employee_2)

print('-' * 100)

print(f"Total salary of all employees: {company.total_salary()} euro")

print('-' * 100)

print(f"Average salary of all employees: {company.average_salary()} euro")

print('-' * 100)

company.remove_emploee(1000)
print("After removing employee with id 1000:")
company.print_employees()

print('-' * 100)

company_2.add_emploee(manager_1)
company_2.add_emploee(manager_2)
company_2.add_emploee(wg_2)
company_2.print_employees()
print("Total numbers of employees:", company_2.quantity())

print('-' * 100)

print(f"Total salary of all employees: {company_2.total_salary()} euro")

print('-' * 100)

print(f"Average salary of all employees: {company_2.average_salary()} euro")

print('-' * 100)

company_2.remove_emploee(1000)
print("After removing employee with id 1000:")
company_2.print_employees()

print('-' * 100)
