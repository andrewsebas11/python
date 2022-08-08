from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
@app.route('/')
def student():
    return render_template('index.html')

@app.route('/add')
def Addstudent():
    return render_template('add.html')

@app.route('/delete')
def Deletestudent():
    return render_template('delete.html')

@app.route('/update')
def Updatestudent():
    return render_template('updatefield.html')

@app.route('/saveupdaterecord',methods=["POST", "GET"])
def Updatestudent1():
    return render_template('update.html')



@app.route("/vadd")
def viewadd():
    con = sqlite3.connect("student.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from studentdetails")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

@app.route("/saveadddetails", methods=["POST", "GET"])
def saveAdd():
    msg = "msg"

    if request.method == "POST":
        try:
            print("Haiiiiii")
            a = request.form["Id"]

            b= request.form["Name"]
            c = request.form["M1"]
            d = request.form["M2"]
            e = request.form["M3"]
            total= int(c)+int(d)+int(e)
            avg= total/3
            print(a,b,c,d,e,total,avg)
            with sqlite3.connect("student.db") as con:
                cur = con.cursor()
                print("kkk")
                cur.execute("INSERT into studentdetails (Id, name,m1,m2,m3,total,average) values (?,?,?,?,?,?,?)", (a, b, c, d, e, total, avg))
                con.commit()
                msg = "Added Successfully"
        except:
            con.rollback()
            msg = "Number cannot be added"
        finally:
            print(msg)
            return render_template("sucess.html", msg=msg)
            con.close()

@app.route("/DeleteStudent", methods=["POST"])
def deleterecord():
    id = int(request.form["id"])
    print(id)
    with sqlite3.connect("student.db") as con:
        try:
            cur = con.cursor()
            sql=f"delete from studentdetails where id={id}"
            print(sql)
            cur.execute(sql)
            msg = "record successfully deleted"
            print(msg)
        except:
            msg = "can't be deleted"
        finally:
            return render_template("sucess.html", msg=msg)



@app.route('/updaterecord',methods=["POST", "GET"])
def updatestudentdetails():
    msg = "msg"
    print("hiiiiiiiiiiii")
    if request.method == "POST":
        try:
            a = int(request.form["id"])
            b = request.form["Name"]
            c = request.form["M1"]
            d = request.form["M2"]
            e = request.form["M3"]
            total = int(c) + int(d) + int(e)
            avg = total / 3
            with sqlite3.connect("student.db") as con:
                cur = con.cursor()
                cur.execute(f"update studentdetails set  name='{b}',m1={c},m2={d},m3={e},total={total},average={avg} where Id={a}")
                # cur.execute("update users set Name=?,M1=?,M2=?,M3=? where UID=?", (uname, contact, uid))
                con.commit()
                msg = "update done successfully"
        except:
            con.rollback()
            msg = "numbers cannot be  updated"
        finally:
            return render_template("sucess.html", msg=msg)
            con.close()




app.run(debug=True, port=1357)
