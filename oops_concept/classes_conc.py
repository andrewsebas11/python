class emp1:
    print("welcome")
    print("oops concept")
    print("Hi")


class emp2:
    pass


class employee:
    name = 'xyz'
    ID = 1234

    def printemp(self):
        print(self.name)
        print(self.ID)


e = employee()
e.printemp()
print(e.name)
print(e.ID)
print(employee.name)


class ConstructExample:
    def __init__(self, id, name):
        print('-------------')
        self.id = id
        self.name = name
        print(self.id)
        print(self.name)


c = ConstructExample(2, 'andrew')
d = ConstructExample(3, 'mark')


class Header:
    def __init__(self):
        print("welcome to student program")
        print('----------------')


class Footer:
    def __init__(self):
        print('-----------------')


class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printmess(self):
        print(f"id={self.id} and name={self.name}")


h = Header()
s1 = Student(1, 'andrew')
s1.printmess()
f = Footer()

h1 = Header()
s2 = Student(2, 'mark')
s2.printmess()
f1 = Footer()

