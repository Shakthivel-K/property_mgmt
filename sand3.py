import mysql.connector
from mysql.connector import Error
def create_connection(host_name,port_name,user_name,user_password,db_name):
    connection=None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            port=port_name,
            user=user_name,
            database=db_name,
            passwd=user_password
        )
        print("Connection to mysql successful")
    except Error as e:
        print("The error '{}' occurred".format(e))
    return connection
connection =create_connection("localhost","3306","admin","password","sand")
def insertion_query(connection,database_query):

    cursor=connection.cursor()
    result = None
    try:
        cursor.execute(database_query)
        result=cursor.fetchall()
        connection.commit()
        return result
    except Error as e:
        print("The error '{}' occurred".format(e))
        return "error"
def selection_query(connection,database_query):
    cursor=connection.cursor()
    result =None
    try:
        cursor.execute(database_query)      
        result =cursor.fetchall()
        return result        
    except Error as e:
        print("The error '{}' occurred".format(e))
        return "error"
create_users = "select * from tab;"
print(selection_query(connection, create_users));
reader =open ("commands.txt","r")
writer = open("crcted.txt","a")
string=""
i=0
for rows in reader:
    cursor=connection.cursor()
    result = None
    row=rows
    i+=1
    k=1
    while k==1:
        try:
            cursor.execute(row)
            result=cursor.fetchall()
            connection.commit()
            writer.write(row)
            writer.write("\n")
            k=0
        except Error as e:
            print("The error '{}' occurred".format(e))
            k=1
            print ("Query number",i)
            print("Enter new value to replace "+row+"\n")
            row=input("")
        




        