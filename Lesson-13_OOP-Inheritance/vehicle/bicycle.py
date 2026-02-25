from vehicle import Vehicle

class Bicycle(Vehicle):
    def __init__(self, vehicle_type, brand, model, year, weight, color, bicycle_type):
        super().__init__(vehicle_type, brand, model, year, weight, color)
        self.bicycle_type = bicycle_type

    def __str__(self):
        return f"{super().__str__()}, Bicycle Type: {self.bicycle_type}"
