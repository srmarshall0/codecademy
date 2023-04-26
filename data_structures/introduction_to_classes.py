# create student class
class Student:
  def __init__(self, name, year):
    self.name = name 
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

  def get_average(self):
    return average(self.grades)

# create grade class 
class Grade:
  minimum_passing = 65
  # define a constructor 
  def __init__(self, score):
    self.score = score
  # define passing method 
  def is_passing(self, score):
    if Grade(score) >= 65:
      print("You are passing")
    else:
      print("You are not passing")

# create instances 
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(100))