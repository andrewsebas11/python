class Grandfather():
    def __init__(self, gname, gage):
        self.gname = gname
        self.gage = gage
    def printgrandfatherdetails(self):
        print(f"Name = {self.gname} and Age = {self.gage}")
class Father(Grandfather):
    def __init__(self,gname, gage, fname, fage):
        Grandfather.__init__(self, gname, gage)
        self.fname = fname
        self.fage = fage
    def printfatherdetails(self):
        Grandfather.printgrandfatherdetails(self)
        print(f"Name = {self.fname} and Age = {self.fage}")
class Son(Father):
    def __init__(self, gname,gage,fname, fage, name, age):
        Father.__init__(self, gname,gage,fname, fage)
        self.name = name
        self.age = age
    def printsondetails(self):
        Father.printfatherdetails(self)
        print(f"Name = {self.name} and Age = {self.age}")
g = Son('Rathinam', 90, 'Innaci', 55,'ANdrew', 26)
g.printsondetails()
