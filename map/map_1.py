#o = list(map(functionname/lambda, argumentlist))

def square(num1):
    return num1**2


def cube(num1):
    return num1**3


def addition(num1, num2):
    return num1+num2


y = lambda a: 3.14*(a**2)

z = lambda a: a**4

a = square(5)
b = square(6)
c = square(7)
d = cube(5)
e = cube(6)
f = cube(7)
print(a, b, c)
print(d, e, f)
g = addition(2, 3)
h = addition(2, 7)
i = addition(2, 17)
print(g, h, i)
print(y(2), y(3), y(4))
print(z(2), z(3), z(4))

l1 = [5, 6, 7]
map1 = list(map(square, l1))
print(map1)
map2 = list(map(cube, l1))
print(map2)
map3 = list(map(addition, l1, l1))
print(map3)
l2 = [2, 3, 4]
map4 = list(map(y, l2))
print(map4)
map5 = list(map(z, l2))
print(map5)

