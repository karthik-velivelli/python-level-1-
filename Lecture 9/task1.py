class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age )
        self.roll_number = roll_number
    def study(self):
        self.display_info()
        print(f"Roll number : {self.roll_number}")
        print(f"Student is Studying")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def teach(self):
        self.display_info
        print(f"Subject: {self.subject}")
        print("Teacher is teaching")

student1 = Student("Rahul", 20, 101)
teacher1 = Teacher("Priya", 35, "Python")
student1.study()

        
        


        