f = open('t.txt', 'w')
l = ['Hi\n', 'I am\n', 'from Chennai\n']
f.write('Hi Welcome\n')
f.writelines(l)
f.close()

a = open('t.txt', 'r')
z = a.read()
print(z)

# b = a.readlines()
# print(b)

# c = a.readline()
# print(c)