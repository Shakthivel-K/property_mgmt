from flask import Flask
from flask import render_template
from flask import request
from main import *
db="sand"
image = "/static/person.png"
Aadharimage = "/static/aadharimage.jpg"
app=Flask(__file__,template_folder="webpages")
@app.route("/")
def index():
    return render_template("home.html")

        

if __name__ == "_main_":
    app.run()