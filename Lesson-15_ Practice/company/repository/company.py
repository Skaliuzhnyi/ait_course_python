class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_emploee(self, employee):
        # TODO: Implement employee addition logic

        # for e in self.employees:
        #     if e.id == employee.id:
        #         return False
        
        e = self.find_emploee(employee.id)
        if e is None:
            self.employees.append(employee)
            return True
        return False

    def remove_emploee(self, employee_id):
        # TODO: Implement employee remove logic
        
        for i, employee in enumerate(self.employees):
            if employee.id == employee_id:
                del self.employees[i]
                return True
        return False

    def find_emploee(self, employee_id):
        # TODO: Implement employee search logic
        
        for employee in self.employees:
            if employee.id == employee_id:
                return employee
        return None

    def total_salary(self):
        # TODO: Calculate total salary of all employees
        
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.calculate_salary()
        return total_salary

    def average_salary(self):
        # TODO: Calculate average salary of all employees
        
        if len(self.employees) == 0:
            return 0
        return self.total_salary() / len(self.employees)

    def quantity(self):
        # TODO: Calculate the numbers of employees
        
        return len(self.employees)

    def print_employees(self):
        # TODO: Print employees details
        
        print(f"Employees in - '{self.name}':")
        for employee in self.employees:
            print(employee)


