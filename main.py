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
class queries:
    def execute(self,table_name,mode,database_query,connector):
        self.table_name=table_name
        self.mode=mode
        self.database_query=database_query
        cursor=connector.connection.cursor()
        result = None
        try:
            cursor.execute(database_query)
            result=cursor.fetchall()
            connector.connection.commit()
        except Error as e:
            print("The error '{}' occurred".format(e))
            result="error"
        if (mode=="insertion"):
            cursor.commit();
        return result
        


root_connection=connections();
root_connection.create_connection("localhost","3306","admin","password","sand")
query_buffer=queries()
statement=query_buffer.execute("tabs","selection","select * from tab;",root_connection);
print (statement)
def parse_result(connector,query):
    if (query.result=="error"):
        #do something about it later
        print("error")
    else :
        print(query.result)
    
