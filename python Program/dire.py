import os
print(os.getcwd())
os.chdir('/Users/apple/Desktop/python Program/pythongui')
print(os.getcwd())
print(os.listdir())
os.mkdir('NewPython1')
print(os.listdir())
os.rename("sample4.jpg", "Sample5.jpg")
print(os.listdir())
os.rename("NewPython2", "deletefolder2")
print(os.listdir())
#os.remove("LICENSE")
print(os.listdir())
os.rmdir("deletefolder1")
print(os.listdir())
os.chdir('/Users/apple/Desktop/python Program/templates')
filelist=os.listdir()
print(filelist)