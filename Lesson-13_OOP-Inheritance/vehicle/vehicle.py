# TODO Homework Vehicle class hierarchy example.
# Inheritances of Vehicle class: Car, Motorcycle, Bicycle, Bus.

class Vehicle:
    def __init__(self, vehicle_type, brand, model, year, weight, color):
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.model = model
        self.year = year
        self.weight = weight
        self.color = color

    def __str__(self):
        return f"Type: {self.vehicle_type}, Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Weight: {self.weight}kg, Color: {self.color}"
