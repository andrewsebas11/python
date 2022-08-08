import numpy as np
m = []
n = []
for a in range(0,3):
    t = []
    for b in range(0,3):
        z = []
        for c in range(0,3):
            v = int(input("enter the number"))
            t.append(v)
            z.append(t)
        m.append(z)

for a in range(0,3):
    t = []
    for b in range(0,3):
        z = []
        for c in range(0,3):
            v = int(input("enter the row"))
            t.append(v)
            z.append(t)
        n.append(z)

print(m)
print(n)
a = np.array(m)
print(a)
print('-------------------------------------------------')
b = np.array(n)
print(b)
print('-------------------------------------------------')
print(a+b)