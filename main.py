from logging import root
import mysql.connector
from mysql.connector import Error
def log_message(msg):
    file=open("message.txt")
    file.write(msg)
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
        self.result = None
        try:
            cursor.execute(database_query)
            self.result=cursor.fetchall()
            connector.connection.commit()
        except Error as e:
            print("The error '{}' occurred".format(e))
            self.result="error"
        if (mode=="insertion"):
            cursor.commit();
        return self.result    
class results:
    def __init__(self,header,query):
        self.header=header
        self.query=query  
        self.degree=len(header)
        self.cardinality=len(query.result)

    def display_cmd(self):
        for i in self.header:
            print(i,end='\t')
        print('\n')
        for i in self.query.result:
            print(i,end='\t')
        print('\n')
        ##write functions as per requirement

root_connection=connections();
root_connection.create_connection("localhost","3306","admin","password","sand")
query_buffer=queries()
query_buffer.execute("tab","selection","select * from tab;",root_connection);
#print (query_buffer.result)
def parse_result(connector,query):
    if (query.result=="error"):
        return []
        print("error")
    else :
        query1=queries()
        num_attributes=len(query1.execute(query.table_name,"selection","desc "+query.table_name+";",connector))
        table_data_query=queries()
        table_data_query.execute("information_schema.columns","selection","select column_name from information_schema.columns where table_name = \""+query.table_name+"\";",connector)
        header=()
        for i in range(0,num_attributes,1):
            header+=table_data_query.result[i]
        res=results(header,query)
        return res



    
