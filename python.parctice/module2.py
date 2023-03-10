
# n=int(input('enter a number:'))
# def evennumbers():
# # n=int(input('enter a number:'))
#     for i in range(n):
#         if i%2==0:
#             print(i,'even number')
#         else:
#             print(i, 'odd number')
# if __name__ == "__main__":

#    evennumbers()
# import module1 as m
# print(m.x)
# m.add(10,20)
# m.product(5,3)
# import module1

# marks ={}
# # threshold = 50
# pass_count = 0
# fail_count = 0

# students= dict()
# n=int(input("how many students are there :"))
# pass_student = 0
# fail_student = 0
# for i in range(n):
#     hall=input("enter a roll nuber:")
#     name=input("enter a student name:")
#     # for j in range(5):
#     mark=int(input("enter a student marks:"))
#     if mark>=35 and mark<=100:
#             pass_student+=1
#             print('your exam passed:')
#     else:
#             fail_student+=1
#             print('your exam failed:')
#             print("Number of students who passed", pass_student)
#             print("Number of students who failed: ", fail_student)
          
# # list=[1,2,3,4,5,6]
# # list.reverse() 
# # print(list)
# # print(list[2::-1]+list[5:--1]
# import json

# a Python object (dict):
# int_dict = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# search_key={'name','age','city'}
# search_key['name']=int(input("etnter your name:" ))
# if search_key in int_dict:
#      print("Key exist in JSON data")

# else:
#     print("Key doesn't exist in JSON data")

# students= dict()
# n=int(input("how many students are there :"))
# pass_student = 0
# fail_student = 0
# for i in range(n):
#     hall=input("enter a roll nuber:")
#     name=input("enter a student name:")
#     # for j in range(5)
#     mark=int(input("enter a student marks:"))
#     if mark>=35 and mark<=100:
#             pass_student+=1
#             print('your exam passed:')
#     else:
#             fail_student+=1
#             print('your exam failed:')
            
# print("Number of students who passed", pass_student)
# print("Number of students who failed: ", fail_student)   

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='venkat',password='venkat1817.')
# print(mydb)
# student_data={'name':'venkat',
#    'age':'22 ',
#    'college':'s.v.university'}
# e=len(student_data)
# for i in range(e):
#     i=input("Enter key :")
#     if i in a:
#         print("Key exist in JSON data")
#         # print(a[i])
#     else:
#         print("Key doesn't exist in Json data")     
            
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='root@123',database='demo')
# mycursor=mydb.cursor()
# # mycursor.execute("CREATE DATABASE studentdata") 
# # mycursor.execute("CREATE TABLE studentdata(name VARCHAR(255),address VARCHAR(225),mobileno INT(10),collegeName VARCHAR(255),email VARCHAR(255)(10))")
# mycursor.execute("SELECT *FROM studentdata ")
# sql=("INSERT INTO studentdata((name,addres,mobileno,collegeName,email)VALUES(%s,%s,%s,%s,%s,)")
# val=('pavan','npkunta','9014776855','sdhr','dvenkat@1123')
# val= ('kadiri','npkunta')
# ('reddy','kadiri','9014776855','svu','dvenkat@1123')
# ('reddy','kadiri','9014776855','svu','dvenkat@1123')

# mycursor.execute(sql,val)


# a={
# "FirstName": "venkat",
# "LastName": "reddy",
# "employeeID": 7995910832,
# "Designation": "python developer",}
# e=len(a)
# for i in range(e):
#     var=input("Enter  a key :")
#     if var in a:
#         print("Key exist in JSON data")
#         print(a[var])
#     else:
#         print("Key doesn't exist in Json data")

# list=int(input("enter a list:[]"))
# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# e=len(birthdays)
# for i in range(e):
#     var=input("enter a name:")
#     if var in birthdays:
#         print ("birthday" )
#         print(birthdays[var])
#     else:
#         print('birthday boy not there')


# dictionary = {
#                  '1': 'sunday',
#                  '2': 'monday',
#                  '3': 'tuesday',
#                  '4': 'wednesday',
#                  '5': 'thursday',
#                  '6': 'friday',
#                  '7': 'saturday'

#              }
# #dictionary[input('enter the number: ')]
# a=len(dictionary)

# for i in range(a):
#  day=input('Enter the day number: ')
#  if day=='1':
#      Break:
#  if day in dictionary:
#     print("exiting your day")  
#     print(dictionary[day])
#  else:
#     print("invaild day")

# spam = {}
# spam['first key'] = 'value'
# spam['second key'] = 'value'
# spam['third key'] = 'value'
# print(list(spam))

# spam = {'color': 'red', 'age': 42}
# # for v in spam.items():
# print(spam.items())
# print(spam.items())
# print(spam.items()
# import json

# python object(dictionary) to be dumped
# dict1 ={
# 	"emp1": {
# 		"name": "venkat",
# 		"college": "sdhr",
# 		"age": "22",
# 		"salary": "0000"
# 	},
# 	"emp2": {
# 		"name": "pavan",
# 		"college": "skr",
# 		"age": "22",
# 		"salary": "10000"
# 	},
# }
# v=len(dict1)

# for i in range(v):
#  emp=input('Enter any key: ')

#  if emp in dict1:
#     print("exiting your day")  
#     # print(dict1.keys())
#  else:
#     print("not exit day")
# print(dict1.keys())
# print(dict1[emp1])

# theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
# 'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
# def printBoard(board):
#  print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#  print('-+-+-')
#  print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#  print('-+-+-')
#  print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# printBoard(theBoard)
#
# 
# mylist = [1,2,3,5,2,1,6,6,4] 
# print(len(mylist))
# print(set(mylist))
# list1 = [] 
# duplicate  = [] 
# for i in mylist:
#     if i not in list1:
#         list1.append(i)
#     else:
#         duplicate.append(i) 
       
# print("List of duplicates", duplicate)
# # print("Unique list", list1)
# print(len(duplicate))

# print('What is your list?') 
# mylist = input()
# print('You will be ' + str(int(mylist) + 1) + ' in a year.')
# a = list(map(int,input("Enter the list : ").split()))

# print("List is - ", a)
# Israining = input("Enter yes and no: ") 
# if Israining == "yes": 
#     print("Have umbrella")
# elif Israining == "no": 
#    print ("Go outside.")
# else: 
#    print("Please enter yes or no.") 


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern




# def pypart(n):
	
# 	# outer loop to handle number of rows
# 	# n in this case
# 	for i in range(0, n):
	
# 		# inner loop to handle number of columns
# 		# values changing acc. to outer loop
# 		for j in range(0, 1+i):
		
# 			# printing stars
# 			print("* ",end="")
	
# 		print("\r")

# # Driver Code
# n = 5
# pypart(n)


# s=input("enter a name:")
# print(s==s[-1::-1])
# s = "malayalam"
 
# if s:
#     print("Yes")
# else:
#     print("No")

# Python program to find second largest
# number in a list
 
# creating list of integer type
# Python program to find second largest number
# in a list

# list1 = [10, 20, 4, 45,54, 99]
# list = set(list1)
# list.remove(max(list))
# print(max(list))

# lst=[1,2,3,4,5,6,7,8]
# len(lst)
# print(lst)
# n=int(input('enter a number:'))
# n2=int(input('enter a second number:'))
# nl=[]
# for x in range(125):
#     if (x%125==0) :
#         nl.append((x))
# print(nl)

# import boto3
# import mysql.connector

# # Set up AWS credentials
# aws_access_key_id = 'AKIAUGNVM5B7QUBRQOBB'
# aws_secret_access_key = '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'
# region_name = 'us-east-1'

# Set up MySQL credentials
# db_host = 'localhost'
# db_user = 'root'
# db_password = 'root@123'
# db_name = 'ec2-server'

# # Connect to AWS EC2 client
# ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# # Get list of EC2 instances and their attributes
# instances = ec2_client.describe_instances()

# # Connect to MySQL database
# db = mysql.connector.connect(db_host=localhost, db_user=root, db_password=root@123, db_name=ec2-server)
# cursor = db.cursor()

# # Create table in MySQL database
# cursor.execute("CREATE TABLE IF NOT EXISTS ec2_instances (instance_id VARCHAR(20), instance_type VARCHAR(20), vpc_id VARCHAR(20))")
# print(cursor)
# Insert instance data into MySQL table
# for reservation in instances['Reservations']:
#     for instance in reservation['Instances']:
#         instance_id = instance['InstanceId']
#         instance_type = instance['InstanceType']
#         vpc_id = instance['VpcId']
#         cursor.execute("INSERT INTO ec2_instances (instance_id, instance_type, vpc_id) VALUES (%s, %s, %s)", (instance_id, instance_type, vpc_id))

# # Commit changes to MySQL database and close connection
# db.commit()
# db.close()


# import boto3,pprint,sqlite3 
# client = boto3.client('ec2')
# response =client.describe_instances()
# pprint.pprint(response)
# con = sqlite3.connect("instances.db")    
# con.execute("create table instances(InstanceType TEXT NOT NULL, InstanceId TEXT UNIQUE NOT NULL, VpcId TEXT NOT NULL)")  
# for i in response.values():
#     if type(i)==list:
#         a=i[0]
#         for j in a.values():
#             if len(j)==0:
#                 continue 
#             else:
#                 b=j[0]
#                 # print(type(b))
#                 # pprint.pprint(b)
#                 c=b['InstanceId']
#                 d=b['InstanceType']
#                 e=b['VpcId']
#                 break
# con = sqlite3.connect("instances.db")   
# cur = con.cursor()  
# cur.execute("INSERT into instances(InstanceType, InstanceId, VpcId) values (?,?,?)",(d,c,e))  
# con.commit() 
# con.close()



# # import boto3,pprint,sqlite3 
# # client = boto3.client('ec2')
# # response =client.describe_instances()
# # pprint.pprint(response)
# # con = sqlite3.connect("instan.db")    
# # con.execute("create table instan(InstanceType TEXT NOT NULL, InstanceId TEXT UNIQUE NOT NULL, VpcId TEXT NOT NULL)")  
# # for i in response.values():
# #     if type(i)==list:
# #         a=i[0]
# #         for j in a.values():
# #             if len(j)==0:
# #                 continue 
# #             else:
# #                 b=j[0]
# #                 # print(type(b))
# #                 # pprint.pprint(b)
# #                 c=b['InstanceId']
# #                 d=b['InstanceType']
# #                 e=b['VpcId']
# #                 break
# # con = sqlite3.connect("instan.db")   
# # cur = con.cursor()  
# # cur.execute("INSERT into instan[(InstanceType, InstanceId, VpcId) values (?,?,?)",(d,c,e))
            
          
# # con.commit() 
# import boto3,pprint,sqlite3
# client = boto3.client('ec2')
# response =client.describe_instances()
# data =sqlite3.connect('instances.db')
# data.execute("create table instances( KeyName TEXT NOT NULL, InstanceId TEXT UNIQUE  NOT NULL , InstanceType TEXT NOT NULL)")
# k=response['Reservations']
# if type(k)==list:
#     a=len(k)
    
#     for i in range(a):
#         b=k[i]
       
#         c=b['Instances']
   
#         if len(c)>=1:
#             d=c[0]
#            data= sqlite3.connect("instance.db")
#             h =data.cursor()  
#             h.execute("INSERT into instances(KeyName,InstanceId,'InstanceType) values (?,?,?)",(d['KeyName'],d['InstanceId'],d['InstanceType']))  
#             data.commit()        
#             data.close()
import random, sys
print('PAPERS, ROCKER, SCIRRORS')

#the variables keep track of the wins, losses, and ties
wins = 0
losses = 0
ties = 0

while True:
    print('%s wins, %s losses, %s ties %(wins,losses,ties)')
    while True:
        print('Enter your move (r)ock (p)aper (s)cissors (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #exit the program

        if playerMove == 'r' or playerMove == 's' or playerMove == 'p':
            break
        print('type one of r,p,s and q')