class Flyer:
    def __init__(self, max_height):
        self.max_height = max_height

    def fly(self):
        print(f"Flying up to {self.max_height} metres")


class Fighter:
    def __init__(self, strength):
        self.strength = strength

    def fight(self):
        print(f"Fighting with strength {self.strength}")


class Hero(Flyer, Fighter):
    def __init__(self, hero_name, max_height, strength):
        Flyer.__init__(self, max_height)
        Fighter.__init__(self, strength)
        self.hero_name = hero_name

    def introduce(self):
        print(f"I am {self.hero_name}")


hero = Hero("Skyblaze", 500, 80)
hero.introduce()
hero.fly()
hero.fight()