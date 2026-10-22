class Academic:
    def __init__(self, math_marks, science_marks):
        self.math_marks = math_marks
        self.science_marks = science_marks

    def calculate_total(self):
        return self.math_marks + self.science_marks

class Sports:
    def __init__(self, sport_name, sport_score):
        self.sport_name = sport_name
        self.sports_score = sport_score

    def display_sports(self):
        print(f"Sport: {self.sport_name}")
        print(f"Sports Score: {self.sports_score}")

class Student(Academic, Sports):
    def __init__(self, student_name, math_marks, science_marks, sport_name, sport_score):
        Academic.__init__(self, math_marks, science_marks)
        Sports.__init__(self, sport_name, sport_score)
        self.student_name = student_name

    def display_results(self):
        print(f"Student Name: {self.student_name}")
        academic_total = self.calculate_total()
        print(f"Academic Total: {academic_total}")
        self.display_sports()
        final_score = academic_total + self.sports_score
        print(f"Final score: {final_score}")

student = Student("Rahul", 85, 90, "Football", 15)
student.display_results()
