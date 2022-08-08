class Father():
    def __init__(self, fname, fage):
        self.fname = fname
        self.fage = fage
    def printfatherdetails(self):
        print(f"Name = {self.fname} and Age = {self.fage}")
class Son1(Father):
    def __init__(self, fname, fage, sname, sage):
        Father.__init__(self, fname, fage)
        self.sname = sname
        self.sage = sage
    def printson1details(self):
        Father.printfatherdetails(self)
        print(f"Name = {self.sname} and Age = {self.sage}")
class Son2(Father):
    def __init__(self, fname, fage, aname, aage):
        Father.__init__(self, fname, fage)
        self.aname = aname
        self.aage = aage
    def printson2details(self):
        Father.printfatherdetails(self)
        print(f"Name = {self.aname} and Age = {self.aage}")
class Son3(Father):
    def __init__(self, fname, fage, bname, bage):
        Father.__init__(self, fname, fage)
        self.bname = bname
        self.bage = bage
    def printson3details(self):
        Father.printfatherdetails(self)
        print(f"Name = {self.bname} and Age = {self.bage}")
s1 = Son1('Innaci', 55, 'Jacob', 28)
s1.printson1details()
s2 = Son2('Innaci', 55, 'Andrew', 26)
s2.printson2details()
s3 = Son3('Innaci', 55, 'Anjali', 22)
s3.printson3details()
