import mysql.connector
host="localhost"
user="pythonuser"
password="python123"
db="shruthi"
conn=mysql.connector.connect(host=host, user=user, password=password, db=db)
cur=conn.cursor()
#1.single row - fetchone()
#2.all row - fetchAll()
#3.no of row - fetchmany(size)
cur.execute("select * from employeee") #function in cursor
res=cur.fetchone()
print(res)