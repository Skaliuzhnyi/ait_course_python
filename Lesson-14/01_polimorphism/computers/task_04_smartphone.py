from computers.task_03_laptop import Laptop


class Smart_phone(Laptop):
    def __init__(self, cpu, ram, ssd, brand, hours, weight, imai):
        super().__init__(cpu, ram, ssd, brand, hours, weight)
        self.imai = imai

    def __str__(self):
        return f"{super().__str__()}, IMAIL: {self.imai}"


class SmartPhone(Completer):
