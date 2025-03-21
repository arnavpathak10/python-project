import mysql.connector
from time import sleep
import datetime
try:
    conn = mysql.connector.connect(user = "root", password = "root", host = "localhost", port = 3306)
    if(conn.is_connected()):
        print("Connected Successfully to mysql server")
except:
    print("Unable to make connection")

sql = "CREATE DATABASE visitor_record"
try:
    myc = conn.cursor()
    myc.execute(sql)
    print("Database created")
except:
    print("Unable to create database")


#creating table 
config = {"user" : "root", "password" : "root", "database" : "visitor_record", "host" : "localhost", "port" : "3306"}
try:
    connection = mysql.connector.connect(**config)
    if (connection.is_connected):
        print("Successfully connected to database")
except:
    print("Unable to connect with database")
sql1 = "CREATE TABLE visitor(Sr_no INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25), Address VARCHAR(50), Date varchar(20), Time VARCHAR(20), Contact INT)"
try:
    myc_table = connection.cursor()
    myc_table.execute(sql1)
    print("Table created")
except:
    print("Unable to create table")


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
        add = input("Enter your address : ").title()
        date = datetime.datetime.now().date()
        time = datetime.datetime.now().time()
        contact = int(input("Enter Mobile number : "))
        insert_record(name, add, date, time, contact)
    
    sleep(4)
    inp = input("\nDo you want to display all records (yes/no) : ")
    if(inp.lower()=="yes" or inp.lower()=="y"):
        query = "SELECT * FROM visitor"
        mycur_obj = connection.cursor()
        mycur_obj.execute(query)
        rows = mycur_obj.fetchall()
        for row in rows:
            print(f"sr.no : {row[0]:5d}  Name : {row[1]:15s}  Address : {row[2]:15}  Date : {row[3]:10}  Time : {row[4]:10}  Contact : {row[5]:10}")

   
