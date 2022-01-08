from flask import Flask
from flask import render_template
from flask import request
from main import *
db="sand"
app=Flask(__name__,template_folder="webpages")
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/sell")
def sell_index():
    return render_template("sell_index.html")

@app.route("/login_1",methods=["GET","POST"])#seller
def login_page():
    print("Vers")
    if (request.method=="POST"):
        print("posted")
        receptionist=connections()
        receptionist.create_connection("localhost","3306","root","password",db)
        query=queries()
        uname=request.form.get("uname")
        pwd=request.form.get("pwd")
        if (uname[0]=="o"):
            query.execute("login_info","selection","select * from login_info where code like 'o%';",receptionist)
            query_result=parse_result(receptionist,query)
            query_result.display_cmd()
            login_page_2()
        else:
            return render_template("login_1.html",msg1="Username Invalid")
            
    
    return render_template("login_1.html")
@app.route("/login_2",methods=["GET","POST"])#buy
def login_page_2():
    if (request.method=="POST"):
        pass
    return render_template("login_2.html")
@app.route("/login_3",methods=["GET","POST"])#refer
def login_page_3():
    if (request.method=="POST"):
        pass
    return render_template("login_3.html")
@app.route("/signup")
def signup():
    return render_template("signup.html")


        

if __name__ == "__main__":
    app.run()


