import mysql.connector
from time import sleep
import datetime
try:
    conn = mysql.connector.connect(user = "root", password = "root", host = "localhost", port = 3306)
    if(conn.is_connected()):
        print(True)
except:
    print("unable to make connection")

sql = "CREATE DATABASE visitor_record"
try:
    myc = conn.cursor()
    myc.execute(sql)
except:
    print("unable to create database")
myc.close()
conn.close()"""

#creating table 
config = {"user":"root", "password":"root", "database":"visitor_record", "host":"localhost", "port":3306}
try:
    connection = mysql.connector.connect(**config)
    if(connection.is_connected()):
        print("Connection Established")
except:
    print("unable to connect")
"""sql1 = "CREATE TABLE visitor(Sr_no INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25), Address VARCHAR(50), Date varchar(20), Time VARCHAR(20), Contact INT)"
try:
    mycur = connection.cursor()
    mycur.execute(sql1)
    print("Table created")
except:
    print("Unable to create table")
mycur.close()
connection.close()

#enter visitor records
def insert_record(n, a, d, t, c):
    sql_query = "INSERT INTO visitor(Name, Address, Date, Time, Contact) VALUES(%(name)s, %(add)s, %(date)s, %(time)s, %(contact)s)"
    params =  {"name" : n, "add" : a, "date" : d, "time" : t, "contact" : c}
    try:
        cur_obj = connection.cursor()
        cur_obj.execute(sql_query, params)
        connection.commit()
        print(f"You can go Details Inserted successfully, Row Inserted : {cur_obj.rowcount}")
    except:
        connection.rollback()
        print("Unable to insert row! Insert again")

while True:
    inp = input("\nDo you want to enter records (yes/no) : ")
    if(inp.lower()=="yes" or inp.lower()=="y"):
        name = input("Enter your name : ").title()
        add = input("Enter your add : ").title()
        date = datetime.datetime.now().date()
        time = datetime.datetime.now().time()
        contact = int(input("Enter Mobile number : "))
        insert_record(name, add, date, time, contact)
    sleep(6)
    inp = input("\nDo you want to display all records (yes/no) : ")
    if(inp.lower()=="yes" or inp.lower()=="y"):
        query = "SELECT * FROM visitor"
        mycur_obj = connection.cursor()
        mycur_obj.execute(query)
        rows = mycur_obj.fetchall()
        for row in rows:
            print(f"sr.no : {row[0]:5d}  Name : {row[1]:15s}  Address : {row[2]:15}  Date : {row[3]:10}  Time : {row[4]:10}  Contact : {row[5]:10}")


   
