class Father():
    def __init__(self, fname, fage):
        self.fname = fname
        self.fage = fage
    def printfatherdetails(self):
        print(f"Name = {self.fname} and Age = {self.fage}")
class Mother():
    def __init__(self, mname, mage):
        self.mname = mname
        self.mage = mage
    def printmotherdetails(self):
        print(f"Name = {self.mname} and Age = {self.mage}")
class Son(Father, Mother):
    def __init__(self,fname, fage, mname, mage, name, age):
        Father.__init__(self, fname, fage)
        Mother.__init__(self, mname, mage)
        self.name = name
        self.age = age
    def printsondetails(self):
        Father.printfatherdetails(self)
        Mother.printmotherdetails(self)
        print(f"Name = {self.name} and Age = {self.age}")
s = Son('Innaci', 55, 'Jothi', 53, 'Andrew', 26)
s.printsondetails()