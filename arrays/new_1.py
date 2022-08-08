from tkinter import *
window = Tk()
window.title('vicky')
window.minsize(width=200,height=400)
window.maxsize(width=400,height=800)
cb=Checkbutton(window,text='male')
cb.pack()
window.mainloop()