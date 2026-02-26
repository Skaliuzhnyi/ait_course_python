from computers.task_02_computer import Computer


class Laptop(Computer):
    def __init__(self, cpu, ram, ssd, brand, hours, weight):
        super().__init__(cpu, ram, ssd, brand)
        self.hours = hours
        self.weight = weight

    def __str__(self):
        return f"{super().__str__()}, Battery: {self.hours}, Weight: {self.weight}"
