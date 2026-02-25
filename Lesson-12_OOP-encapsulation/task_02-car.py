# Car: producer, model, year, color

class Car:
    def __init__(self, producer, model, year, color):
        self.producer = producer
        self.model = model
        self.year = year
        self.color = color

    def __str__(self) -> str:
        return f"producer: {self.producer}, model: {self.model}, year: {self.year}, color: {self.color}"

    def change_color(self, new_color):
        self.color = new_color


car_1 = Car('Honda', 'Accord', '2004', 'Black')
car_2 = Car('VW', 'Passat', '2026', 'White')

print(car_1.producer)
print(car_2.producer)

print('-' * 70)

print(car_1)
print(car_2)

print('-' * 70)

print(f'{car_1}\n{car_2}')

print('-' * 70)

cars = [car_1, car_2]
for car in cars:
    print(car)

print('-' * 70)

car_2.change_color('Red')
print(car_2)
print(car_2.color)

print('-' * 70)

print('=== Copy auto 1 ===')

car_1_copy = car_1
car_1_copy.change_color('Blue')
print(car_1)
print(car_1_copy)
