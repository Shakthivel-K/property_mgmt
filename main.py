import mysql.connector
from mysql.connector import Error
class connections:
    def create_connection(self,host_name,port_name,user_name,user_password,db_name):
        self.connection=None
        self.host_name=host_name
        self.port_name=port_name
        self.user_name=user_name
        self.user_password=user_password
        self.db_name=db_name
        try:
            self.connection = mysql.connector.connect(
                host=host_name,
                port=port_name,
                user=user_name,
                database=db_name,
                passwd=user_password
                )
            print("Connection to mysql successful")
        except Error as e:
            print("The error '{}' occurred".format(e))
root_connection=connections();
root_connection.create_connection("localhost","3306","admin","password","sand")
def insertion_query(connector,database_query):
    cursor=connector.connection.cursor()
    result = None
    try:
        cursor.execute(database_query)
        result=cursor.fetchall()
        connector.connection.commit()
        return result
    except Error as e:
        print("The error '{}' occurred".format(e))
        return "error"
def selection_query(connector,database_query):
    cursor=connector.connection.cursor()
    result =None
    try:
        cursor.execute(database_query)      
        result =cursor.fetchall()
        return result        
    except Error as e:
        print("The error '{}' occurred".format(e))
        return "error"
command = "select * from tab;"
print(selection_query(root_connection, command))
command ="desc tab;"
print (selection_query(root_connection,command))
tups=selection_query(root_connection, command)


