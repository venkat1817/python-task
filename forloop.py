# eor loop using even numbers print. 
# list=[1,2,3,4,5,6,7,8,9,10,1]
# for i in list:
#    lst1=[]
#    if i%2==0:
#       lst1.append(i)
#       print(lst1)list=[1,2,3,4,5,6,7,8,9,10,1]


#3 or same in forloop.
# for i in range(10):
#     print(i)
    
# for i in range(0,10):
#     print(i)
    
# for i in range(0,10,1):
#     print(i)


# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20
# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
 column = [] # Create a new column.
 for y in range(HEIGHT):
    if random.randint(0, 1) == 0:
        column.append('#') # Add a living cell.
 else:
    column.append(' ') # Add a dead cell.
 nextCells.append(column) # nextCells is a list of column lists.
while True: # Main program loop.
 print('12345') # Separate each step with newlines.
 currentCells = copy.deepcopy(nextCells)
