class Student:
  def __init__(self, new_name, new_grade):
    self.name = new_name
    self.grade = new_grade

  def average(self):
    return sum(self.grade) / len(self.grade)

student_one = Student("Oketa Fred", [1, 2, 3, 4])

print(student_one.name)
print(student_one.average())