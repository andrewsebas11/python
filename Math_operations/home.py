from flask import Flask, render_template, request, redirect, url_for, flash
from databaseprogram import *

app = Flask(__name__)
@app.route('/')
def cal():
    return render_template('index.html')


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/sub')
def sub():
    return render_template('sub.html')


@app.route('/mul')
def multiply():
    return render_template('mul.html')


@app.route('/div')
def division():
    return render_template('div.html')

@app.route('/additiondetails',methods=["POST", "GET"])
def additiondetails():
    msg = "msg"
    print("hiiiiiiiiiiii")
    if request.method == "POST":
        try:
            a = request.form["number1"]
            b = request.form["number2"]
            result = int(a)+int(b)
            with sqlite3.connect("mathop.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into addition (num1,num2,result) values (?,?,?)", (a, b, result))
                con.commit()
                msg = "Addition done successfully"
        except:
            con.rollback()
            msg = "numbers cannot be  added"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

@app.route('/substractiondetails',methods=["POST", "GET"])
def substractiondetails():
    msg = "msg"
    if request.method == "POST":
        try:
            a = request.form["number1"]
            b = request.form["number2"]
            result = int(a)-int(b)
            with sqlite3.connect("mathop.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into sub (num1,num2,result) values (?,?,?)", (a, b, result))
                con.commit()
                msg = "Substraction done successfully"
        except:
            con.rollback()
            msg = "numbers cannot be  added"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

@app.route('/multiplicationdetails',methods=["POST", "GET"])
def multiplicationdetails():
    msg = "msg"
    if request.method == "POST":
        try:
            a = request.form["number1"]
            b = request.form["number2"]
            result = int(a)*int(b)
            with sqlite3.connect("mathop.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into mul (num1,num2,result) values (?,?,?)", (a, b, result))
                con.commit()
                msg = "Multiplication done successfully"
        except:
            con.rollback()
            msg = "numbers cannot be  added"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

@app.route('/divisiondetails',methods=["POST", "GET"])
def divisiondetails():
    msg = "msg"
    if request.method == "POST":
        try:
            a = request.form["number1"]
            b = request.form["number2"]
            result = int(a)/int(b)
            with sqlite3.connect("mathop.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into div (num1,num2,result) values (?,?,?)", (a, b, result))
                con.commit()
                msg = "Division done successfully"
        except:
            con.rollback()
            msg = "numbers cannot be  added"
        finally:
            return render_template("success.html", msg=msg)
            con.close()




app.run(debug=True, port=1658)