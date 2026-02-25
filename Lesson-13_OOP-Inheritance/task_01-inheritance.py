class Computer:
    def __init__(self, cpu, ram, ssd, brand):
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
        self.brand = brand

    def __str__(self):
        return f"Barand: {self.brand}, CPU: {self.cpu}, RAM: {self.ram}, SSD: {self.ssd}"


class Laptop:
    def __init__(self, cpu, ram, ssd, brand, hours, weight):
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
        self.brand = brand
        self.hours = hours
        self.weight = weight

    def __str__(self):
        return f"Barand: {self.brand}, CPU: {self.cpu}, RAM: {self.ram}, SSD: {self.ssd}, Battery: {self.hours}, Weight: {self.weight}"


class Laptop2(Computer):
    def __init__(self, cpu, ram, ssd, brand, hours, weight):
        super().__init__(cpu, ram, ssd, brand)
        self.hours = hours
        self.weight = weight

    def __str__(self):
        return f"{super().__str__()}, Battery: {self.hours}, Weight: {self.weight}"


class Smart_phone(Laptop2):
    def __init__(self, cpu, ram, ssd, brand, hours, weight, imai):
        super().__init__(cpu, ram, ssd, brand, hours, weight)
        self.imai = imai

    def __str__(self):
        return f"{super().__str__()}, IMAIL: {self.imai}"


comuter_1 = Computer('M4', 64, '2Tb', 'Apple')
laptop_1 = Laptop('M4', 64, '2Tb', 'Apple', '23 uhr', 1.433)
print("My dream computer - ", comuter_1)
print("My dream laptop - ", laptop_1)

print('-' * 100)

laptop_2 = Laptop2('M4', 128, '2Tb', 'Apple', '23 uhr', 2.433)
print("My dream laptop - ", laptop_2)

print('-' * 100)

smartphone = Smart_phone('ios', 128, 512, 'Iphone', '48 uhr', .333, 32444033)
print("My dream Smart Phone - ", smartphone)

print('-' * 100)
