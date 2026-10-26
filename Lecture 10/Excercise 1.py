class Temperature:
    def __init__(self, celsius):
        if type(celsius) == int or type(celsius) == float: 
            self.celsius = celsius
        else:
            print("Cannot assign value. Please enter a integer or a float value")
            self.celsius = 0
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

    def __eq__(self, other):
        return (self.celsius == other.celsius)

    def __ne__(self, other):
        return (self.celsius != other.celsius)
    
    def __lt__(self, other):
        return (self.celsius < other.celsius)

    def __gt__(self, other):
        return (self.celsius > other.celsius)

    def __le__(self, other):
        return (self.celsius <= other.celsius)

    def __ge__(self, other):
        return (self.ceslsius >= other.celsius)



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