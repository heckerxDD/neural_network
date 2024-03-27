import math 
import matplotlib.pyplot as plt
import numpy as np

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def set_grade(self, new_grade):
        if new_grade >= 0 and new_grade <= 10:
            self.grade = new_grade
        else:
            print("Invalid Grade")

class Kid(Student):
    def __init__(self, name, age, grade, school_name):
        super().__init__(name, age, grade)
        self.school = school_name
        self.toys = []

    def add_toy(self, toy):
        if len(self.toys) < 4:
            self.toys.append(toy)
        else:
            print("Too many toys")

s1= Student('John', 25, 8)
s2= Student('Mary', 26, 9)
s3= Student('Peter', 27, 10)
k1 = Kid('Jane', 5, 10, 'School A')

k1.add_toy('car')
print(k1.toys)