from flask import Flask
from flask import render_template
from flask import request
from main import *

app=Flask(__name__,template_folder="webpages")
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/sell")
def sell_index():
    return render_template("sell_index.html")

@app.route("/login_1",methods=["GET","POST"])
def login_page():
    if (request.method=="POST"):
        receptionist=connections()
    return render_template("login_1.html")
@app.route("/login_2",methods=["GET","POST"])
def login_page_2():
    if (request.method=="POST"):
        pass
    return render_template("login_2.html")
@app.route("/login_3",methods=["GET","POST"])
def login_page_3():
    if (request.method=="POST"):
        pass
    return render_template("login_3.html")


        

if __name__ == "__main__":
    app.run()


