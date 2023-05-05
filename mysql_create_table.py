import mysql.connector as sql

conn = sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db")
cur = conn.cursor()

cmd = "CREATE TABLE employees (\
    empid varchar(30) not null, \
    empname VARCHAR(30) NOT NULL,\
    empgender VARCHAR(30), \
    empphone VARCHAR(30), \
    empbdate VARCHAR(30))"

cur.execute(cmd)
conn.close()



