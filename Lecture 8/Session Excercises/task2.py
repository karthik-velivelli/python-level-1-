class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employe_id, basic_salary):
        Person.__init__(self, name, age)
        self.employee_id = employe_id
        self.basic_salary = basic_salary

    def display_employee(self):
        self.display_person()
        print(f"Employee ID: {self.employee_id}")
        print(f"Basic Salary: {self.basic_salary}")

class Manager(Employee):
    def __init__(self, name, age, employee_id, basic_salary, bonus, allowance):
        Employee.__init__(self, name, age, employee_id, basic_salary)
        self.bonus = bonus
        self.allowance = allowance

    def calculate_salary(self):
        return self.basic_salary + self.bonus +self.allowance


    def display_details(self):
        self.display_employee()
        print(f"Bonus: {self.bonus}")
        print(f"Allowance: {self.allowance}")
        print(f"Final Salary: {self.calculate_salary()}")





manager = Manager("Rahul", 30, "EMP101", 50000, 10000, 5000)
manager.display_details()
        
    