class Father():
    def __init__(self, fname, fage):
        self.fname = fname
        self.fage = fage

    def printfatherdetails(self):
        print(f"Father name = {self.fname} and age = {self.fage}")


class Son(Father):
    def __init__(self,fname, fage, name, age):
        Father.__init__(self, fname, fage)
        self.name = name
        self.age = age

    def printsondetails(self):
        print(f"Son name = {self.name} and age = {self.age}")


# f = Father('Innaci', 55)
# s = Son('Andrew', 26)
# f.printfatherdetails()
# s.printsondetails()

s = Son('Innaci', 55, 'Andrew', 26)
s.printfatherdetails()
s.printsondetails()
