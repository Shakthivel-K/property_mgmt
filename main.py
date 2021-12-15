class connections:
    def create_connection(self,host_name,port_name,user_name,user_password,db_name):
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


#################33
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
