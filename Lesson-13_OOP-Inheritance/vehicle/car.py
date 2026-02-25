from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, vehicle_type, brand, model, year, weight, color, doors):
        super().__init__(vehicle_type, brand, model, year, weight, color)
        self.doors = doors

    def __str__(self):
        return f"{super().__str__()}, Doors: {self.doors}"
