"""class Student:
    def _init_(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        return f"Hi, I am {self.name}, a {self.age} year old {self.major} major"

    def hi(self):
        return f"Hi, my name is {self.name}"

s1 = Student("Alice", 20, "CS")
s2 = Student("Bob", 22, "Math")

print(s1.introduce())
print(s2.introduce())
print(s2.hi())

class TeachingFellow(Student):
    def _init_(self,name, age, major, cohort):
        super()._init_(name, age, major)
        self.age = age - 3
        self.cohort = cohort


    def introduction(self):
        return f"{super().introduce()}. I am also the best TF here!"

tf1 = TeachingFellow("Kayla", 23, "Physics")
print(tf1.introduce())"""


"""
You use it to specify that you want to use the parent methods within the child class. 
For example, look at the introduce method. 
You use super() to specify you want the parent’s introduce() method.

"""

# Python Tutor


# Linked List
"""


"""

class Node:
    def _init_(self, value):
        self.value = value
        self.next = None

x = Node(2)
y = Node(4)
x.next = y
print(x.value)


