# Python code to demonstrate table creation and 
# insertions with SQL 

# importing module 
import sqlite3 

# connecting to the database 
connection = sqlite3.connect("databases/myTable.db") 

# cursor 
crsr = connection.cursor() 

# SQL command to create a table in the database 
sql_command = '''CREATE TABLE emp ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE);'''

# execute the statement 
crsr.execute(sql_command) 

# SQL command to insert the data in the table 
sql_command = '''INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");'''
crsr.execute(sql_command) 

# another SQL command to insert the data in the table 
sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
crsr.execute(sql_command) 

# To save the changes in the files. Never skip this. 
# If we skip this, nothing will be saved in the database. 
connection.commit() 

# close the connection 
connection.close() 
