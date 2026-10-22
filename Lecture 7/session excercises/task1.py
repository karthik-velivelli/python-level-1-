class BikeV0:
    def __init__(self, wheels, fuel_capacity):
        self.wheels = wheels
        self.fuel_capacity = fuel_capacity

    def display(self):
        print(f"Number of wheels: {self.wheels}, Fuel capacity: {self.fuel_capacity}")


class BikeV1(BikeV0):
    def __init__(self, wheels, fuel_capacity, battery):
        super().__init__(wheels, fuel_capacity)
        self.battery = battery

    def charge_battery(self):
        self.battery = 100

    def check_battery(self):
        return self.battery