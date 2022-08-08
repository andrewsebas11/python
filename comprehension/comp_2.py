l1 = []
l2 = set()
l3 = {}
for a in range(1, 11):
    if a%2 == 0:
        l1.append('even')
        l2.add('even')
        l3[a] = 'even'
    else:
        l1.append('odd')
        l2.add('odd')
        l3[a] = 'odd'
print(l1)
print(l2)
print(l3)
print(['even'if a % 2 == 0 else'odd' for a in range(1, 11)])
print({a: 'even'if a % 2 == 0 else'odd' for a in range(1, 11)})
print({'even'if a % 2 == 0 else'odd' for a in range(1, 11)})