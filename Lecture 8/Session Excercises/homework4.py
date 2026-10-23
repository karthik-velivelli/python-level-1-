class Package:
    def __init__(self, sender, weight_kg):
        self.sender = sender
        self.weight_kg = weight_kg

    def base_charge(self):
        return self.weight_kg * 30

    def display_package(self):
        print(f"Sender: {self.sender}")
        print(f"Weight: {self.weight_kg} kg")


class ExpressPackage(Package):
    def __init__(self, sender, weight_kg, express_fee):
        super().__init__(sender, weight_kg)
        self.express_fee = express_fee

    def charge_before_insurance(self):
        return self.base_charge() + self.express_fee


class InsuredPackage(ExpressPackage):
    def __init__(self, sender, weight_kg, express_fee, insurance_percent):
        super().__init__(sender, weight_kg, express_fee)
        self.insurance_percent = insurance_percent

    def insurance_charge(self):
        return (self.charge_before_insurance() * self.insurance_percent) // 100

    def final_bill(self):
        return self.charge_before_insurance() + self.insurance_charge()

    def display_bill(self):
        self.display_package()
        print(f"Base Charge: {self.base_charge()}")
        print(f"Express Fee: {self.express_fee}")
        print(f"Insurance: {self.insurance_charge()}")
        print(f"Final Bill: {self.final_bill()}")


# Testing Sample Input 1
parcel1 = InsuredPackage("Asha", 4, 50, 10)
parcel1.display_bill()

print()  # Blank line between tests

# Testing Sample Input 2
parcel2 = InsuredPackage("Ravi", 10, 80, 20)
parcel2.display_bill()