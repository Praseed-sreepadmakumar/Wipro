import mysql.connector
host="localhost"
user="root"
password="fearse"
database="wipro_database"

conn=mysql.connector.connect(host=host,user=user,password=password,database=database)
cursor=conn.cursor()
print("Connected to the database successfully")
query="select * from wipro_database.employee"
cursor.execute(query)
result=cursor.fetchall()
for row in result:
    print(row)