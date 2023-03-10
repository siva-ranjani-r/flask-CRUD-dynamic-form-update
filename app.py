from flask import Flask,render_template,request,redirect,url_for
import sqlite3 as sql

app=Flask("__name__")

@app.route("/",methods=["POST","GET"])
def insert():
    if request.form.get('id')!=None:
        id=request.form.get("id")
        user=request.form.get("username")
        conn=sql.connect("user.db")
        cur = conn.cursor()
        cur.execute("insert into data (id,username) values (?,?)",(int(id),user))
        conn.commit()
    return render_template("index.html")

@app.route("/update/<id>",methods=["POST","GET"])
def update1(id):
    if request.form.get("id")!=None:
        user1=request.form.get("username")
        conn=sql.connect("user.db")
        cur=conn.cursor()
        cur.execute("UPDATE DATA SET USERNAME=? WHERE ID=?",(user1,int(id)))
        conn.commit()
        return render_template("index.html")
    conn=sql.connect("user.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from data where ID=?",(int(id),))
    a=cur.fetchone()
    return render_template("create.html",data=a)

if __name__=="__main__":
    app.run(debug=True)