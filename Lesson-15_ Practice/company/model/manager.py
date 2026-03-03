from company.model.employee import Employee 

class Manager(Employee):
    def __init__(self, id, first_name, last_name, hovers, base_salary, hover_bonus):
        super().__init__(id, first_name, last_name, hovers)
        self.base_salary = base_salary
        self.hover_bonus = hover_bonus
        
    def calculate_salary(self):
        return self.base_salary + self.hover_bonus * self.hovers
        
    # def __str__(self):
    #     return f"{super().__str__()}, salary: {self.calculate_salary()}"
