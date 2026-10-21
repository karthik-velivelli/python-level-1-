class Order:
    def __init__(self):
        self._item = "none"
        self._price = 0
        self._quantity = 0

    def set_item(self, item):
        self._item = item

    def get_item(self):
        return self._item

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_quantity(self, quantity):
        self._quantity = quantity

    def get_quantity(self):
        return self._quantity

    def total(self):
        return self.get_price() * self.get_quantity()

    def display(self):
        print(f"Item: {self.get_item()}")
        print(f"Price: {self.get_price()}")
        print(f"Quantity: {self.get_quantity()}")
        print(f"Total: {self.total()}")