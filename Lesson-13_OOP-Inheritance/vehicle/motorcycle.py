from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, vehicle_type, brand, model, year, weight, color, motorcycle_type):
        super().__init__(vehicle_type, brand, model, year, weight, color)
        self.motorcycle_type = motorcycle_type

    def __str__(self):
        return f"{super().__str__()}, Motorcycle Type: {self.motorcycle_type}"
