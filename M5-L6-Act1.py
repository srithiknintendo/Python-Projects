class Student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks + other.marks
s1 = Student(90)
s2 = Student(80)
print(s1+s2)

class Pizza:
    def __init__(self,slices):
        self.slices = slices
    def __add__(self,other):
        return self.slices + other.slices
p1 = Pizza(4)
p2 = Pizza(5)
print(p1+p2)

