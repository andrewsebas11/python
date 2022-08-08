from tkinter import *
from tkinter.filedialog import askopenfilename


def NewFile():
    print("New File!")


def OpenFile():
    name = askopenfilename()
    print(name)


def About():
    print("This is a simple example of a menu")


root = Tk()
root.title('Filemenu')
root.geometry('400x200')
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()