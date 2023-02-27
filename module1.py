 
# print('hello goodmrng!')
# x=888 
# a=10
# b=20
# def add(a,b): 
#  print("The Sum:",a+b) 
# def product(a,b): 
#  print("The Product:",a*b)
# import json

# import json

# data = {


# e=len(data)
# for i in range(e):
#     var1=input("Enter  a key :")
#     if var1 in data:
#         print("Key exist in JSON data")
#         # print(a[var])
#     else:
#         print("Key doesn't exist in Json data")
        
# list=int(input("enter a list:"))
# eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# print(eggs) 
# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# while True:

#  name = input("enter a name:")
# if name in birthdays:
#  print(birthdays[name] + ' is the birthday of ' + name)
# else:
#  print('I do not have birthday information for ' + name)
#  print('What is their birthday?')
#  bday = input()
#  birthdays[name] = bday
#  print('Birthday database updated.')my_dict = {"Name":[],"Address":[],"Age":[]};
# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# a=len(birthdays)
# for i in range(a):
#  my_name=input("enter a name:")

   
# if my_name in birthdays:
#  print(birthdays[my_name] + ' is the birthday of ' + my_name)
#  print(birthday.items())
# else:
#  print('I do not have birthday information for ' + my_name)
#  print('What is their birthday?')
#  bday = input()
#  birthdays[name] = bday
#  print('Birthday database updated.')
# def eggs(someParameter):
#  someParameter.append('Hello')
#  spam = [1, 2, 3]
# eggs(spam)
# print(spam)
# lst=['a','s','A','d']
# lst.sort(key=str.lower)
# print(lst)

# Israining = input("Enter yes or No: ") 
# if Israining == "yes": 
#     print("Have umbrella")
# elif Israining == "No": 
#    print ("Go outside.")
# else: 
#    print("Please enter yes or no.") 

# lst=['venkar','pavan',1,2,3,4,5,6,7,8]
# print(len(lst))



# import re
# info =input('Enter the Key : ')

# data = {'details':[
#     {
#         'Name':'auto scaling',
#         'max':'234AZ#',
#         'min':'UP@5678',
#         'server':'Amazon'
#     },
#      {
#         'Name':'auto scaling1',
#         'max':'345CZ@',
#         'min':'CZ?1256',
#         'server':'Amazon1'
#     },
#       {
#         'Name':'auto scaling2',
#         'max':'768GT%',
#         'min' :'AW@123w',
#         'server':'Amazon2'
#     },
#        {
#         'Name':'auto scaling3',
#         'max':'asdferty',
#         'min':'EV#8769',
#         'server':'Amazon3'
#     }
# ]
# }
# # if info in data:
# for i,j in data.items():
#     for k in range(len(j)):
#         for a,t  in j[k].items():
#             if t==info:
#                 c=j[k]['min']
#                 d=j[k]['max']
#                 b=j[k]['server']
#                #  print('server =',b)
#                #  print('max =',d)
#                #  print('min =',c)

                    
#                 s=re.fullmatch('[0-9]{3}[A-Z]{2}[^a-zA-Z0-9]',d)
#                 if s==None:
#                     print('Max num is not matching with the regex')
#                 else:
#                     print('max =',d)
            
#                 f=re.fullmatch('[A-Z]{2}[^a-zA-Z0-9][0-9]{4}',c)
#                 if f==None:
#                     print('Min num is not matching with the regex')
#                 else:
#                     print('min =',c)
                    
#                 z=re.fullmatch('[0-9]{1}[A-Z]{1}[a-z]{5}',b)
#                 if z==None:
#                     print('server is not matching with the regex')
#                 else:
#                      print('server =',b)



# list1 = [10, 20, 4, 45,54, 99]
# list = set(list1)
# list.remove(min(list))
# print(min(list))
# list1.remove(list1)
# print(list1)

# import boto3,pprint,mysql

 






# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='root@123',database='demo')

# print(mycursor)
# mycursor.execute("CREATE DATABASE demo") 
# print(mycursor)
# mycursor.execute("CREATE TABLE studentdata(name VARCHAR(255),address VARCHAR(225),mobileno INT(10),collegeName VARCHAR(255),email VARCHAR(255)(10))")
# mycursor.execute("SELECT *FROM studentdata ")
# sql=("INSERT INTO studentdata((name,addres,mobileno,collegeName,email)VALUES(%s,%s,%s,%s,%s,)")
# val=('pavan','npkunta','9014776855','sdhr','dvenkat@1123')





# import mysql.connector

# Creating connection object
# mydb = mysql.connector.connect(
# 	host="localhost",
#     user="root",
#     password="root@123"
# )

# Printing the connection object
# print(mydb)

