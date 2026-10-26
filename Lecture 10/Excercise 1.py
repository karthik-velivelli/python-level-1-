class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __add__(self, other):
        return Temperature(self.celsius + other.celsius)

    def __sub__(self, other):
        return Temperature(self.celsius - other.celsius)

    def __mul__(self, other):
        return Temperature(self.celsius * other.celsius)

    def __truediv__(self, other):
        return Temperature(self.celsius / other.celsius)

    def __floordiv__(self, other):
        return Temperature(self.celsius // other.celsius)

    def __mod__(self, other):
        return Temperature(self.celsius % other.celsius)

    def __pow__(self, other):
        return Temperature(self.celsius ** other.celsius)



    def __str__(self):
        return f"{self.celsius}°C"


t1 = Temperature(30)
t2 = Temperature(7)
print(t1)
print(t1 + t2)
print(t1 - t2)
print(t1 * t2)
print(t1 / t2)
print(t1 // t2)
print(t1 % t2)
print(t1 ** Temperature(2))