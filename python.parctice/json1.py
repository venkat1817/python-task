
# import mysql.connector
# json_data=open("json.py").read()
# # json_obj=mysql.loads(json_data)
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@123",
#     database='venkat'
# )

# # # # Creating an instance of 'cursor' class
# # # # which is used to execute the 'SQL'
# # # # statements in 'Python'
# cursor = mydb.cursor()
# for item in json_data:
#     Name=item.get('name')
#     max=item.get('max')
#     min= item.get('min')
#     server=item.get('srever')
#     cursor.execute("CREATE TABLE venkat(name VARCHAR(255),max VARCHAR(225),min VARCHAR(255),srerver VARCHAR(255))")
# cursor.execute("INSERT INTO venkat(name,max,min,server)VALUES('%s,%s,%s,%s')")
# print(mydb)
# # mydb.commit()
# # mydb.close()
# # # # # Creating a database with a name
# # # # 'geeksforgeeks' execute() method
# # # # is used to compile a SQL statement
# # # # below statement is used to create
# # # # the 'geeksforgeeks' database
# # # cursor.execute("CREATE DATABASE venkat")
# # cursor.execute("CREATE TABLE venkat(name VARCHAR(255),max VARCHAR(225),min VARCHAR(255),srerver VARCHAR(255))")
# # print(mydb)
# # cursor.execute("SHOW DATABASE")
# # # # cursor.execute("SHOW DATABASE") 
# for x in cursor:
#   print(x)
# # sql="INSERT INTO DATA(name,address,mobile No)VALUES(%s,%s,%i)"


