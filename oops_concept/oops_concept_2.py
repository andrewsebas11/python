class Employee:
    def __init__(self, id, name, location, salary):
        self.id = id
        self.name = name
        self.location = location
        self.salary = salary

    def printempdetails(self):
        print(f"ID = {self.id}, Name = {self.name}, Location = {self.location}, salary = {self.salary}")


c = Employee(1, 'Andrew', 'Chennai', 50000)
c.printempdetails()
d = Employee(2, 'Mark', 'Coimbatore', 60000)
d.printempdetails()
e = Employee(3, 'Sebastin', 'Madurai', 70000)
e.printempdetails()
f = Employee(4, 'Sunder', 'Trichy', 80000)
f.printempdetails()
del d.name
c.printempdetails()
