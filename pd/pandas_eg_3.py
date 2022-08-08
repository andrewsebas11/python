import pandas as pd
l = [1, 2, 3, 4, 5, 6]
names = ['a', 'b', 'c', 'd', 'e', 'f']
m1 = [45, 65, 67, 81, 91, 47]
m2 = [11, 13, 15, 16, 17, 19]
m3 = [22, 24, 26, 28, 30, 32]
m4 = [30, 40, 50, 60, 70, 80]
print(l)
print(names)
print(m1)
print(m2)
print(m3)
print(m4)
tab1 = {'Sno': l, 'names': names, 'M1': m1}
print(tab1)
tab2 = {'Sno': l, 'names': names, 'M2': m2}
print(tab2)
tab3 = {'Sno': l, 'names': names, 'M3': m3}
print(tab3)
tab4 = {'Sno': l, 'names': names, 'M4': m4}
print(tab4)
tab5 = {'Sno': l, 'names': names, 'M1': m1, 'M2': m2, 'M3': m3, 'M4': m4}
print(tab5)
df = pd.DataFrame(tab1)
print(df)
print(df.shape)
print(df.head())
print(df.tail())
print(df.describe())
df1 = pd.DataFrame(tab2)
print(df1)
df2 = pd.DataFrame(tab3)
print(df2)
df3 = pd.DataFrame(tab4)
print(df3)
df4 = pd.DataFrame(tab5)
print(df4)
df4['average'] = (df4['M1'] + df4['M2'] + df4['M3'] + df4['M4']) / 4
print(df4)
df4['total'] = df4['M1'] + df4['M2'] + df4['M3'] + df4['M4']
print(df4)