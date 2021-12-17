from flask import Flask,request
from flask import render_template
from main import *
app = Flask(__name__,template_folder='html_files')

@app.route("/")
def index():
    string=query_buffer.execute("tab","selection","select * from tab;",root_connection);
    return render_template("index.html",data=string)
@app.route("/index2")
def index2():
    string=query_buffer.execute("tab","selection","select * from tab;",root_connection);
    return render_template("index2.html",data=string)
@app.route("/forms", methods =["GET", "POST"])
def form_parse():
    if (request.method=="POST"):
        first_name = request.form.get("fname")
        return render_template("basic_form.html",your_name=first_name)
    return render_template("basic_form.html")
    

if __name__ == "__main__":
    app.run()