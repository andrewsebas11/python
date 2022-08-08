from tkinter import *
import sqlite3
conn = sqlite3.connect(r'C:\sqlite3\training.db')
cur = conn.cursor()

root = Tk()
root.title('database storage')
root.geometry('400x200')


def s():
    print(Iov.get(), namev.get(), m1v.get(), m2v.get(), m3v.get())
    sql=f"insert into student values ({Iov.get()},'{namev.get()}',{m1v.get()},{m2v.get()},{m3v.get()})"
    cur.execute(sql)
    cur.close()
    conn.commit()
    root.destroy()

Label(root, text="Io").grid(row=0, column=0)
Iov = IntVar()
Iov.set('')
Entry(root, textvariable=Iov).grid(row=0, column=1)

Label(root, text="name").grid(row=1, column=0)
namev = StringVar()
Entry(root, textvariable=namev).grid(row=1, column=1)

Label(root, text="m1").grid(row=2, column=0)
m1v = IntVar()
m1v.set('')
Entry(root, textvariable=m1v).grid(row=2, column=1)

Label(root, text="m2").grid(row=3, column=0)
m2v = IntVar()
m2v.set('')
Entry(root, textvariable=m2v).grid(row=3, column=1)

Label(root, text="m3").grid(row=4, column=0)
m3v = IntVar()
m3v.set('')
Entry(root, textvariable=m3v).grid(row=4, column=1)

Button(root, text="submit", command=s).grid(row=5, column=0)

root.mainloop()

