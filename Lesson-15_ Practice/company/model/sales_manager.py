from company.model.employee import Employee


class SalesManager(Employee):
    def __init__(self, id, first_name, last_name, hovers, sale_value, percent):
        super().__init__(id, first_name, last_name, hovers)
        self.sale_value = sale_value
        self.percent = percent
        
    def calculate_salary(self):
        return self.sale_value * self.percent
        
    # def __str__(self):
    #     return f"{super().__str__()}, salary: {self.calculate_salary()}"

