#inbuilt polymorphism
a = 5
b = 6
print(a+b)
a = 'xyz'
b = 'cdc'
print(a+b)
l = 'hello'
print(len(l))
l1 = [1, 2, 3, 4]
print(len(l1))


#polymorphism with function
def addnumber(num1=0, num2=0):
    return num1 + num2


a = addnumber(5, 4)
b = addnumber(5)
c = addnumber()
print(a)
print(b)
print(c)


#polymorphism with classes
class USA():
    def population(self):
        print("It has a dense population")

    def countrytype(self):
        print("American")


class India():
    def population(self):
        print("It has a dense population")

    def countrytype(self):
        print("Indian")

u = USA()
i = India()

# u.population()
# u.countrytype()
#
# i.population()
# i.countrytype()

for a in (u, i):
    a.population()
    a.countrytype()

