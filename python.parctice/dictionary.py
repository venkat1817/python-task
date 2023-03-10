
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





##Json format

# a={'a':'s',
#    'd':'f',
#    'c':'d'}
# e=len(a)
# for i in range(e):
#     var=input("Enter  a key :")
#     if var in a:
#         print("Key exist in JSON data")
#         # print(a[var])
#     else:
#         print("Key doesn't exist in Json data")





# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# while True:
#     name = input('Enter a name: ')

  
#     if name in birthdays:
#             print(birthdays[name] + ' is the birthday of ' + name)
#     else: 
#         print('I do not have birthday information for ' + name)
#     print('What is their birthday?')
#     bday = input()
#     birthdays[name] = bday
#     print('Birthday database updated.')

##for using dict method
# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# # birthdays.get['name'].get{"name_one":'venkat','name_two':'pavan'}

# print((birthdays.values()))
# for i in birthdays.keys():


# spam = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# for i in spam.items():
#   print(i)

# spam = {'color': 'red', 'age': 42}
# spam.keys()
# print(list(spam.keys()))                       #['color', 'age']

# spam = {'color': 'red', 'age': 42}
# spam.keys()
# print((spam.keys()))                       #dict_keys(['color', 'age'])




# spam = {'color': 'red', 'age': 22}
# for k,v in spam.items():
#     print('Key: ' + k+ ' Value: ' + str(v))




# spam = {'name': 'Zophie', 'age': 7}
# 'name' in spam.keys()

# print('Zophie' in spam.values())
# print('color' in spam.keys())
# print('color' not in spam.keys())
# print('color' in spam)



# picnicItems = {'apples': 5, 'cups': 2}
# print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
# print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')                #I am bringing 2 cups.
                                                                                      # I am bringing 0 eggs.

# print( 2.rjust(20, '*'))

# print('Hello'.ljust(20, '-'))

# list =[1,2,3,4,5,6]
# print(list[2::-1]+list[-1:2:-1])
