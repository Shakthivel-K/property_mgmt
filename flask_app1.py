from flask import Flask
from flask import render_template
from flask import request
from flask.helpers import url_for
from flask.wrappers import Request
from werkzeug.utils import redirect
from main import *
db="sand"
image = "/static/person.png"
Aadharimage = "/static/aadharimage.jpg"
app=Flask(__name__,template_folder="webpages")
@app.route("/")
def index():
    return render_template("home.html")
@app.route("/login_1",methods=["GET","POST"])
def buyerlogin():
    if (request.method=="POST"):
        query_buffer.execute("login_info","selection","SELECT * FROM login_info;",root_connection)
        res=parse_result(root_connection,query_buffer)
        Username=request.form.get("uname")
        Password=request.form.get("pwd")
        if (Username[0]!="b" or (Username[1]=="r")):
            return render_template("login_1.html",msg1="Enter Valid Details")
        for tuples in query_buffer.result:
            if (tuples[0]==Username) and (tuples[1]==Password):
                return render_template("home.html")
        return render_template("login_1.html",msg1="Enter Valid Details")
    return render_template("login_1.html",msg1="Username")
@app.route("/login_2",methods=["GET","POST"])
def ownerlogin():
    if (request.method=="POST"):
        query_buffer.execute("login_info","selection","SELECT * FROM login_info;",root_connection)
        res=parse_result(root_connection,query_buffer)
        Username=request.form.get("uname")
        Password=request.form.get("pwd")
        if Username[0]!="o":
            return render_template("login_2.html",msg1="Enter Valid Details")
        for tuples in query_buffer.result:
            if (tuples[0]==Username) and (tuples[1]==Password):
                return render_template("home.html")
        return render_template("login_2.html",msg1="Enter Valid Details")
    return render_template("login_2.html",msg1="Username")
@app.route("/login_3",methods=["GET","POST"])
def adminlogin():
    if (request.method=="POST"):
        query_buffer.execute("login_info","selection","SELECT * FROM login_info;",root_connection)
        res=parse_result(root_connection,query_buffer)
        Username=request.form.get("uname")
        Password=request.form.get("pwd")
        if Username[0]!="a" or not(Username[0]=="b" and Username[1]=="r"):
            return render_template("login_3.html",msg1="Enter Valid Details")
        for tuples in query_buffer.result:
            if (tuples[0]==Username) and (tuples[1]==Password):
                return render_template("home.html")
        return render_template("login_3.html",msg1="Enter Valid Details")
    return render_template("login_3.html",msg1="Username")
        

if __name__ == "__main__":
    app.run()