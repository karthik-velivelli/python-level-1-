class Burger:
    def __init__(self, burger_name, burger_price):
        self.burger_name = burger_name
        self.burger_price = burger_price

    def describe_burger(self):
        print(f"Burger: {self.burger_name} - {self.burger_price} rupees")


class Drink:
    def __init__(self, drink_name, drink_price):
        self.drink_name = drink_name
        self.drink_price = drink_price

    def describe_drink(self):
        print(f"Drink: {self.drink_name} - {self.drink_price} rupees")


class ComboMeal(Burger, Drink):
    def __init__(self, burger_name, burger_price, drink_name, drink_price):
        Burger.__init__(self, burger_name, burger_price)
        Drink.__init__(self, drink_name, drink_price)

    def combo_price(self):
        return (self.burger_price + self.drink_price) - 20

    def display_combo(self):
        self.describe_burger()
        self.describe_drink()
        print(f"Combo Price: {self.combo_price()} rupees")


# Testing Sample Input 1
combo1 = ComboMeal("Veg Burger", 120, "Cola", 60)
combo1.display_combo()

print()  # Blank line between tests

# Testing Sample Input 2
combo2 = ComboMeal("Cheese Burger", 150, "Lemonade", 40)
combo2.display_combo()