class Grandfather():
    def __init__(self, gname, gage):
        self.gname = gname
        self.gage = gage
    def printgrandfatherdetails(self):
        print(f"Name = {self.gname} and Age = {self.gage}")
class Father(Grandfather):
    def __init__(self, gname, gage, fname, fage):
        Grandfather.__init__(self, gname, gage)
        self.fname = fname
        self.fage = fage
    def printfatherdetails(self):
        Grandfather.printgrandfatherdetails(self)
        print(f"Name = {self.fname} and Age = {self.fage}")
class Mother():
    def __init__(self, mname, mage):
        self.mname = mname
        self.mage = mage
    def printmotherdetails(self):
        print(f"Name = {self.mname} and Age = {self.mage}")
class Son(Father, Mother):
    def __init__(self, gname,gage,fname, fage, mname, mage,  name, age):
        Father.__init__(self, gname,gage,fname, fage)
        Mother.__init__(self, mname, mage)
        self.name = name
        self.age = age
    def printsondetails(self):
        Father.printfatherdetails(self)
        Mother.printmotherdetails(self)
        print(f"Name = {self.name} and Age = {self.age}")
s = Son('rathinam', 90, 'Innaci', 55, 'Jothi', 53, 'Andrew', 26)
s.printsondetails()