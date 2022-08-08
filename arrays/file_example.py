from tkinter import *
from tkinter.filedialog import askopenfilename
root = Tk()
root.title('Filemenu')
root.geometry('400x200')
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="New window")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As")
filemenu.add_command(label="Page setup")
filemenu.add_command(label="Print")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

editmenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo")
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_command(label="Find")
editmenu.add_command(label="Find next")
editmenu.add_command(label="Find previous")
editmenu.add_command(label="Replace")
editmenu.add_command(label="Go To")
editmenu.add_command(label="Select all")
editmenu.add_command(label="Time and Date")
editmenu.add_separator()
editmenu.add_command(label="Font")

viewmenu = Menu(menu, tearoff=False)
menu.add_cascade(label="View", menu=viewmenu)
sub_menu = Menu(viewmenu, tearoff=0)
sub_menu.add_command(label="Zoom in")
sub_menu.add_command(label="Zoom out")
sub_menu.add_command(label="Restore default zoom")
viewmenu.add_cascade(label="Zoom", menu=sub_menu)
viewmenu.add_command(label="Statusbar")
viewmenu.add_command(label="Wordwrap")

root.mainloop()