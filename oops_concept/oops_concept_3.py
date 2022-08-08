'''
class Classmethod:
    @classmethod
    def Classmethodexample(self):
        print("no need object")
    def Classmethod1(self):
        print("I need object")


c = Classmethod()+
c.Classmethodexample()
c.Classmethod()

Classmethod.Classmethodexample()
Classmethod.Classmethod1=classmethod(Classmethod.Classmethod1)
Classmethod.Classmethod1()
'''


class geeks:
    course = 'DSA'

    def purchase(obj):
        print("Puchase course : ", obj.course)


geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()


class Student:
    # create a variable

    name = "Geeksforgeeks"

    # create a function

    def print_name(obj):
        print("The name is : ", obj.name)

    # create print_name classmethod


# before creating this line print_name()
# It can be called only with object not with class

Student.print_name = classmethod(Student.print_name)

# now this method can be called as classmethod
# print_name() method is called a class method
Student.print_name()

# Python program to demonstrate
# use of a class method and static method.

from datetime import date


class Person:

    def __init__(self, name, age):
        self.name = name

        self.age = age

        # a class method to create a

    # Person object by birth year.

    @classmethod
    def fromBirthYear(self, name, year):
        print(name, date.today().year - year)

    def display(self):
        print("Name : ", self.name, "Age : ", self.age)


person = Person('mayank', 21)
person.display()
Person.fromBirthYear('andrew', 1996)
Person.fromBirthYear('Innaci', 1967)
Person.fromBirthYear('Jothi', 1969)
Person.fromBirthYear('Jacob', 1994)
Person.fromBirthYear('Anjali', 2000)