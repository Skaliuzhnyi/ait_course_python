class Employee:
    def __init__(self, id, first_name, last_name, hovers):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.hovers = hovers
        
    def __str__(self):
        return f"id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}, hovers: {self.hovers}, salary: {self.calculate_salary()}"
