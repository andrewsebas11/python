l = []
for a in range(1, 11):
    l.append(a)
    l1 = {}
for a in range(1, 11):
    l1[a] = a**a
print(l)
print(l1)
print([a for a in range(1, 11)])
print({a:a**a for a in range(1, 11)})


l2 = []
for a in range(1, 100):
    if a%2 == 0:
        if a%3 == 0:
            l2.append(a)
print(l2)
print([a for a in range(1, 100) if a%2 == 0 if a%3 == 0])


l4 = []
for a in range(1, 11):
    for b in range(1, 11):
        l4.append(a*b)
print(l4)
print([a*b for a in range(1, 11) for b in range(1, 11)])

l5 = {}
l6 = {}
for a in range(1, 11):
    for b in range(1, 11):
        l5[a] = a*b
        l6[a] = l5
print(l6)
print({a:l5 for a in range(1, 11) for b in range(1, 11)})
print({a:a*b for a in range(1, 11) for b in range(1, 11)})