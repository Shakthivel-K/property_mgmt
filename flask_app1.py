from flask import Flask
from flask import render_template
from flask import request
from main import *
db="sand"
image = "/static/person.png"
Aadharimage = "/static/aadharimage.jpg"
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
        receptionist=connections()#only login tabel access
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

@app.route("/Broker",meathod=["GET","POST"])#broker
def Registration():
    if(request.meathod=="POST"):
        print("posted")
        registration = connections()
        registration.create_connection("localhost","3306","root","password",db)
        query = queries()
        Username = request.form.get("Username")
        Email = request.Form.get("Email")
        Phone_Number = request.Form.get("Phone Number")
        Aadhar_Number = request.Form.get("Aaahar Number")
        Phone_Number2 = request.Form.get("Phone Number2")
        Password = request.Form.get("Password")
        Phone_Number3 = request.form.get("Phonenumber2")
        if(Username[0]=='br'):
            reader =open("brokercounter.txt","r")
            writer = open("brokercounter.txt","w")
            k = reader.read()
            k = int(k)+1
            brokercode = "b"+str(k)
            writer.write(k)
            writer.close()
            reader = open("phonecounter.txt","r")
            writer = open("phonecounter.txt","r")
            q = reader.read()
            q = int(q)+1
            phone_number_code = "p"+str(q)

            reader =open("realiablitycounter.txt","r")
            writer = open("realiablitycounter.txt","w")
               
            rr = reader.read()
            rr = int(rr)+1
            rating = rr
        

            query.execute("insert into buyer("+brokercode+","+Username+","+phone_number_code+","+Aadhar_Number+","+Aadharimage+","+image","+Email+","+"image"+",\"good\");")
            query.execute("inser into phone_number("+phone_number_code+","+Phone_Number+","+Phone_Number2+","+Phone_Number3+");")
         
        elif(Username[0]=='b'and  Username[1]!="r"):
            reader =open("buyercounter.txt","r")
            writer = open("buyercounter.txt","w")
            k = reader.read()
            k = int(k)+1
            buyercode = "b"+str(k)
            writer.write(k)
            writer.close()
            reader = open("phonecounter.txt","r")
            writer = open("phonecounter.txt","r")
            q = reader.raed()
            q = int(q)+1
            phone_number_code = "p"+str(q)
            query.execute("insert into buyer("+buyercode+","+Username+","+phone_number_code+","+Aadhar_number+","+image+","+email+");")
            query.execute("inser into phone_number("+phone_number_code+","+Phone_Number+","+Phone_Number2+","+Phone_Number3+");")
            query_result = parse_result(registration,query)
            
        elif(username[0]=='a'):
            reader =open("admincounter.txt","r")
            writer = open("admincounter.txt","w")
            k = reader.read()
            k = int(k)+1
            admin_code = "a"+str(k)
            reader = open("phonecounter.txt","r")
            writer = open("phonecounter.txt","r")
            q = reader.read()
            q = int(q)+1
            phone_number_code = "p"+str(q)
            
            query.execute("insert into administrator("+admin_code+","+name+","+phone_number_code+","+Aadhar_number+","+image+","+Aadharimage+","+email+");")
            query.execute("inser into phone_number("+phone_number_code+","+Phone_Number+","+Phone_Number2+","+Phone_Number3+");")
            query_result = parse_result(registration,query)
           
        elif(username[0]=='t'):
            reader =open("tenantcounter.txt","r")
            writer = open("teanantcounter.txt","w")
            k = reader.read()
            k = int(k)+1
            tenant_code = "t"+str(k)
            reader =open("propertysubcode.txt","r")
            writer = open("propertysubcode.txt","w")
            sp = reader.read()
            sp = int(sp)+1
            property_subcode = "sp"+str(sp)

            reader = open("phonenumber.txt","r")
            writer = open("phonenumber.txt","r")
            q = reader.read()
            q = int(q)+1
            phone_number_code = "p"+str(q)
            query.execute("insert into administrator("+tenant_code+","+property_subcode+","+name+","+phone_number_code+","+Aadhar_number+","+Aadharimage+","+image+","+","+email+","+image);")
            query.execute("inser into phone_number("+phone_number_code+","+Phone_Number+","+Phone_Number2+","+Phone_Number3+");")
            
            query_result = parse_result(registration,query)
            
        else:
           reader =open("owner.txt","r")
           writer = open("owner.txt","w")
            k = reader.read()
            k = int(k)+1
            owner_code = "t"+str(k)
            

           reader = open("phonenumber.txt","r")
            writer = open("phonenumber.txt","r")
            q = reader.read()
            q = int(q)+1
            phone_number_code = "p"+str(q)
            query.execute("insert into administrator("+owner_code+","+username+","+phone_number_code+","+Aadhar_number+","+Aadharimage+","+image+","+","+email+","+image+","+"good");")
            query.execute("inser into phone_number("+phone_number_code+","+Phone_Number+","+Phone_Number2+","+Phone_Number3+");")


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

@app.route("/Broker.html",meathods=["GET","POST"])#BROKER
def registre


        

if _name_ == "_main_":
    app.run()