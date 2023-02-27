
import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.
try:
    while True: # The main program loop.
        print('7 ' * indent, end='')
        print('******* reddy')
        time.sleep(0.2) # Pause for 1/10 of a second.
        if indentIncreasing:
 # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
 # Change direction:
                indentIncreasing = False
        else:
 # Decrease the number of spaces:
                indent = indent - 1
                if indent == 0:
 # Change direction:
                    indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
   
# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@123",
# )
# mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE data") 
# # mycursor.execute("CREATE TABLE DATA(name VARCHAR(255),max VARCHAR(225),min VARCHAR(255),srerver VARCHAR(255))")
# # # mycursor.execute("SHOW TABLES ")
# sql="INSERT INTO DATA(name,address,mobile No)VALUES(%s,%s,%i)"
# # # # val=("venkat","rayachoti",9014776855)
# # # # mycursor.execute(sql,val)
# # # # mydb.commit()
# # # for x in mycursor: 
# print(mydb)
 
 
# import mysql.connector

# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@123",
#     database='venkat'
# )

# # # # Creating an instance of 'cursor' class
# # # # which is used to execute the 'SQL'
# # # # statements in 'Python'
# # cursor = mydb.cursor()

# # # # Creating a database with a name
# # # # 'geeksforgeeks' execute() method
# # # # is used to compile a SQL statement
# # # # below statement is used to create
# # # # the 'geeksforgeeks' database
# # # cursor.execute("CREATE DATABASE venkat")
# # cursor.execute("CREATE TABLE venkat(name VARCHAR(255),max VARCHAR(225),min VARCHAR(255),srerver VARCHAR(255))")
# # print(mydb)
# # cursor.execute("SHOW DATABASE")
# # # # cursor.execute("SHOW DATABASE") 
# # for x in cursor:
# #   print(x)



# import mysql.connector

# try:
#     mydb= mysql.connector.connect(host='localhost',
#                                          database='data',
#                                          user='root',
#                                          password='root@123')

#     mySql_insert_query = """INSERT INTO DATA (Id, Name, Price, Purchase_date) 
#                            VALUES (%s, %s, %s, %s) """

#     details = [(4, 'HP Pavilion Power', 1999, '2019-01-11'),
#                          (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
#                          (6, 'Microsoft Surface', 2330, '2019-07-23')]

#     cursor = mydb.cursor()
#     cursor.executemany(mySql_insert_query, details)
#     mydb.commit()
#     print(cursor.rowcount, "Record inserted successfully into Laptop table")

# except mysql.connector.Error as error:
#     print("Failed to insert record into MySQL table {}".format(error))

# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL mydbis closed")
