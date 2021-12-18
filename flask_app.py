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

@app.route("/login",methods=["GET","POST"])
def login_page():
    if (request.method=="POST"):
        receptionist=connections()
        

if __name__ == "__main__":
    app.run()


