class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 20:
            self.grades.append(grade)
        else:
            print("Note invalide.")

    def get_average(self):
        if len(self.grades) == 0:
            return 0

        return sum(self.grades) / len(self.grades)


# Tester le programme
student = Student("Samuel")

student.add_grade(14)
student.add_grade(18)
student.add_grade(12)

print(student.grades)
print(f"Moyenne : {student.get_average():.2f}")