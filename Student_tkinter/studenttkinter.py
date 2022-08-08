from tkinter import*
import sqlite3
conn = sqlite3.connect(r'D:\python\Student_tkinter\std.db')
cur=conn.cursor()

root = Tk()
root.title('Student Form')
root.geometry('400x200')


def s():
    print(Idv.get(), namev.get(), m1v.get(), m2v.get(), m3v.get())
    if m1v.get()>=35 and m2v.get()>=35 and m3v.get() >= 35:
        sql = f"insert into pass1 values ({Idv.get()},'{namev.get()}',{m1v.get()},{m2v.get()},{m3v.get()})"
        print(sql)
        cur.execute(sql)
        cur.close()
        conn.commit()
    else:
        sql = f"insert into fail1 values ({Idv.get()},'{namev.get()}',{m1v.get()},{m2v.get()},{m3v.get()})"
        print(sql)
        cur.execute(sql)
        cur.close()
        conn.commit()


Label(root, text="Id").grid(row=0, column=0)
Idv = IntVar()
Idv.set('')
Entry(root, textvariable=Idv).grid(row=0, column=1)

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


Button(root, text="submit", command=s).grid(row=6, column=2)



root.mainloop()