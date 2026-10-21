class Lamp:
    def __init__(self):
        self.brightness = 0

    def set_brightness(self, level):
        self.brightness = level

    def get_brightness(self):
        return self.brightness

    def show(self):
        print(f"Brightness: {self.get_brightness()}")


lamp = Lamp()
a = lamp.get_brightness()
lamp.set_brightness(20)
b = lamp.set_brightness(90)
print(a)
print(b)
print(lamp.get_brightness())
lamp.show()