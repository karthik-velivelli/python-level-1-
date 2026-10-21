class Pet:
    def __init__(self, pet=None):
        if pet is None:
            self._name = "unnamed"
            self._species = "unknown"
            self._age = 0
        else:
            self._name = pet.get_name() if hasattr(pet, 'get_name') else getattr(pet, 'name', "unnamed")
            self._species = pet.get_species() if hasattr(pet, 'get_species') else getattr(pet, 'species', "unknown")
            self._age = pet.get_age() if hasattr(pet, 'get_age') else getattr(pet, 'age', 0)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_species(self, species):
        self._species = species

    def get_species(self):
        return self._species

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def display(self):
        print(f"Name: {self.get_name()}")
        print(f"Species: {self.get_species()}")
        print(f"Age: {self.get_age()}")