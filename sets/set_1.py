#slicing and indexing won't work in sets
s = set()
s1 = {1, 2, 3, 4}
print(type(s))
print(type(s1))
print(s)
print(s1)
s.add(8)
s.add(18)
s.add(21)
print(s)
s2 = {1, 2, 3, 4, 1, 2}
print(s2)
s3 = {'a', 1, 2, 3, 'b', 3, 'b'}
print(s3)
s3.update([8, 81, 27])
print(s3)
s4 = {1, 2, 3, 4, 5, 6}
print(s4)
s4.discard(4)
print(s4)
s4.remove(2)
print(s4)
s5 = {1, 2, 3, 4, 5}
s6 = {2, 3, 1, 4, 9, 8}
s7 = {1, 2, 4, 9, 7, 8}
s8 = s5.union(s6, s7)
s9 = s5.intersection(s6)
s10 = s5.difference(s6)
s11 = s5.symmetric_difference(s7)
print(s8)
print(s9)
print(s10)
print(s11)
#union
s12 = s6 | s7
#
s13 = s7 ^ s5
#intersection
s14 = s7 & s6
#difference
s15 = s8 - s9 - s10
print(s12)
print(s13)
print(s14)
print(s15)

