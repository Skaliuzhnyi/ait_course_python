from company.model.employee import Employee


class WageEmployee(Employee):
    def __init__(self, id, first_name, last_name, hovers, wage):
        super().__init__(id, first_name, last_name, hovers)
        self.wage = wage

    def calculate_salary(self):
        return self.wage * self.hovers

    # def __str__(self):
    #     return f"{super().__str__()}, salary: {self.calculate_salary()}"
