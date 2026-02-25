from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, vehicle_type, brand, model, year, weight, color, capacity):
        super().__init__(vehicle_type, brand, model, year, weight, color)
        self.capacity = capacity

    def __str__(self):
        return f"{super().__str__()}, Capacity: {self.capacity} passengers"
