import os
reader =open("datas.csv","r")
writer=open ("commands.txt","a")
enable_comma=1
table_name=""
ch=[]
for row in reader:
    cells=row.split(',')
    if (cells[0]=="$"):
        table_name=cells[1]
        ch.clear()
        for i in range(2,len(cells),1):
            ch.append(cells[i].rstrip('\n'))
        print(ch)
        
    else:
        #writer.write("insert into "+table_name.rstrip('\n')+" values ("+row.rstrip('\n')+");\n")
        writer.write("insert into "+table_name.rstrip('\n')+" values (");
        for i  in range(0,len(ch),1):
            if ch[i]=="str":
                writer.write("\'"+cells[i]+"\'")
            else :
                writer.write(cells[i])
            if  i==(len(ch)-1):
                    writer.write(");")
            else:
                writer.write(",")
        writer.write("\n")