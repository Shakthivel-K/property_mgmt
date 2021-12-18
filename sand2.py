import os
reader =open("datas.csv","r")
writer=open ("commands.txt","a")
enable_comma=1
table_name=""
for row in reader:
    print(row)
    cells=row.split(',')
    if (cells[0]=="$"):
        table_name=cells[1]
        
    else:
        writer.write("insert into "+table_name.rstrip('\n')+" values ("+row.rstrip('\n')+");\n")
        