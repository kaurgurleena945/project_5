from searching import sequentialSearch, binSearch

import random
import time

list_size = 1000000

list=[]
for _ in range(list_size):
    list.append(random.randint(1, 10000))

found = False
search_over=False

value= int(input("Enter a value to find: "))
while not found and not search_over:

    type = int(input("Linear or binary search? Press 1 for linear, 2 for binary, 3 for exit "))
    if type== 1:
        percentage = int(input("What percentage of the array should linear search cover? "))
    elif type ==2:
        iterations = int(input("How many iterations of binary binary search should be performed? "))
    else:
        break

    if type==1:    
        found = sequentialSearch(list, value, percentage)

        if found:
            print("Value found!")
            break

    elif type==2:
            
        found = binSearch(list, value, iterations )        
        if found:
            print("Value found!")
            break

    print("List is now size of " + str(len(list)))
        
#print(found)

