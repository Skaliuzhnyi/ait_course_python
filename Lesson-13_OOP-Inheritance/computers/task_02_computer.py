class Computer:
    def __init__(self, cpu, ram, ssd, brand):
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
        self.brand = brand

    def __str__(self):
        return f"Barand: {self.brand}, CPU: {self.cpu}, RAM: {self.ram}, SSD: {self.ssd}"

    def is_windows11_compatible(self):
        return self.ram >= 4 and self.ssd >= 3000
