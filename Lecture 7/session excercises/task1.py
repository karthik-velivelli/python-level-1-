class BikeV0:
    def __init__(self, wheels, fuel_capacity):
        self.wheels = wheels
        self.fuel_capacity = fuel_capacity

    def display(self):
        print(f"Number of wheels: {self.wheels}, Fuel capacity: {self.fuel_capacity}")


class BikeV1(BikeV0):
    def __init__(self, wheels, fuel_capacity, battery):
        super().__init__(wheels, fuel_capacity)[cite: 1]
        self.battery = battery[cite: 1]

    def charge_battery(self):[cite: 1]
        self.battery = 100[cite: 1]

    def check_battery(self):[cite: 1]
        return self.battery[cite: 1]