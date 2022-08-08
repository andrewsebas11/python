from tkinter import *
import os.path
import csv
fileexist = os.path.isfile('output1.csv')
print(fileexist)
root = Tk()
root.title('GUI Sample')
root.geometry('400x400')
var=IntVar()
cv= IntVar()
cv1= IntVar()
cv2= IntVar()
cv3= IntVar()
ivd=IntVar()
ivd.set("")


def sel():
    selection = str(var.get())
    print(selection)


def s():


    cvv = cv.get()
    cp = cv1.get()
    jv = cv2.get()
    pv = cv3.get()
    strv = ""
    l = []
    if cvv == 1:
        l.append("C")
    if cp == 1:
        l.append("C++")
    if jv == 1:
        l.append("Java")
    if pv == 1:
        l.append("Python")
    for i in range(len(l)):
        if i == 0:
            v = ""
            v = l[i]
            strv += v
        else:
            v = ","
            v = v + l[i]
            strv += v
    # print(strv)
    print(namev.get(), locationv.get(), salaryv.get(), deptv.get(), designationv.get(), ivd.get(), var.get(), strv)

    if fileexist == True:
        with open('output1.csv', 'w') as file:
            w = csv.writer(file)
            w.writerow(['name', 'location', 'salary', 'dept', 'designation'])
            w.writerow([namev.get(), locationv.get(), salaryv.get(), deptv.get(), designationv.get(), ivd.get(), var.get(), strv])
    else:
        with open('output1.csv', 'w') as file:
            w = csv.writer(file)
            # w.writerow(['ID', 'name', 'age'])
            w.writerow([namev.get(), locationv.get(), salaryv.get(), deptv.get(), designationv.get(), ivd.get(), var.get(), strv])
    root.destroy()


Label(root, text="name").grid(row=0, column=0)
namev = StringVar()
Entry(root, textvariable=namev).grid(row=0, column=1)

Radiobutton(root,text="India",variable=var,value=1,command=sel).grid(row=1,column=0)
Radiobutton(root,text="USA",variable=var,value=2,command=sel).grid(row=1,column=1)
Radiobutton(root,text="UK",variable=var,value=3,command=sel).grid(row=1,column=2)
Radiobutton(root,text="Australia",variable=var,value=4,command=sel).grid(row=1,column=3)


Label(root, text="location").grid(row=2, column=0)
locationv = StringVar()
Entry(root, textvariable=locationv).grid(row=2, column=1)
Label(root, text="salary").grid(row=3, column=0)
salaryv = StringVar()
Entry(root, textvariable=salaryv).grid(row=3, column=1)
Label(root, text="dept").grid(row=4, column=0)
deptv = StringVar()
Entry(root, textvariable=deptv).grid(row=4, column=1)
Label(root, text="designation").grid(row=5, column=0)
designationv = StringVar()
Entry(root, textvariable=designationv).grid(row=5, column=1)

Label(root,text='Employee ID : ').grid(row=6,column=0)
Entry(root,textvariable=ivd).grid(row=6,column=1)


Label(root,text='Interested in : ').grid(row=7,column=0)
Checkbutton(root,text="C",variable= cv).grid(row=8,column=0)
Checkbutton(root,text="C++",variable= cv1).grid(row=8,column=1)
Checkbutton(root,text="Java",variable = cv2).grid(row=8,column=2)
Checkbutton(root,text="Python",variable = cv3).grid(row=8,column=3)


Button(root, text="submit", command=s).grid(row=9, column=0)


root.mainloop()