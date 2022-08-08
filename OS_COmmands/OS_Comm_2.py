import os
print(os.getcwd())
print(os.listdir())
os.chdir(r'C:\Users\hp\OneDrive\Desktop')
c=os.getcwd()
y = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997]
for a in range(len(y)):
    foldername = y[a]
    p = f"{c}\{foldername}"
    folderex=os.path.isdir(p)
    if folderex:
        print("already exit")
    else:
        os.mkdir(str(foldername))
        print(p)
        os.chdir(p)
        for i in range(1,13):
            os.mkdir(str(i))
        os.chdir(c)
# os.rmdir(r'C:\Users\hp\OneDrive\Desktop\1997\1')
# print(c)

