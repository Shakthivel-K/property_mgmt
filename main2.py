from logging import root
import mysql.connector
from mysql.connector import Error
def log_message(msg):
    file=open("message.txt")
    file.write(msg)
class connector:
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
    def __init__(self,connectors,mode):
        self.connectors=connectors
        self.mode=mode
        self.result=[]
        self.cmd=""
    def execute(self,cmd):
        self.cmd=cmd
        cursor=self.connectors.connection.cursor()
        self.result = None
        try:
            cursor.execute(cmd)
            self.result=cursor.fetchall()
            connector.connection.commit()
        except Error as e:
            print("The error '{}' occurred".format(e))
            self.result="error"
        if (self.mode=="insertion"):
            cursor.commit()
        return self.result  

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
