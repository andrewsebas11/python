import pandas as pd
l = [1, 2, 3, 4, 5, 6, 7]
name = ['babu', 'xyz', 'abc', 'xy', 'z', 'z1', 'zz']
print(l)
print(name)
table = {"Sno": l, "names": name}
print(table)
df = pd.DataFrame(table)
print(df)