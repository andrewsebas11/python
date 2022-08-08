import os
#cwd = current working directory
print(os.getcwd())
print(os.listdir())
l = os.listdir()
for a in range(len(l)):
    print(l[a])
os.chdir(r'C:\Users\hp\OneDrive\Desktop')
#chdir = change directory
print(os.getcwd())
print(os.listdir())
l1 = os.listdir()
for a in range(len(l1)):
    print(l1[a])
foldername = input("enter the foldername")
os.mkdir(foldername)
print(os.listdir())