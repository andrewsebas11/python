x = lambda: 'hello'
print(x())
y = lambda a, b: a+b
print(y(2, 3))
z = lambda x = 0: x**2
print(z(5))
print(z())
y1 = lambda r = 0: 3.14*(r**2)
print(y1(2))
print(y1(4))
print(y1())


z1 = lambda: '----'


def print10numbers():
    for a in range(1, 11):
        print(a)
        print(z1())
print(print10numbers())

def largestofthreenumber():
    '''

    :return:
    '''


