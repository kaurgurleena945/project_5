def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def binSearch(mylist, x):
    mylist.sort()
    lower=0
    upper=len(mylist)-1
    while lower <= upper:
        mid = lower + (upper - lower)//2 # find the middle
        # Check if x is present at mid
        if mylist[mid] == x:
            return True #found it- return index

        # If x is greater, ignore left half
        elif mylist[mid] < x:
            lower = mid + 1

        # If x is smaller, ignore right half  else:
        else:
            upper = mid - 1
    # If we reach here, then the element was not present
    return False


############## test code ##############

"""
import random

list_size = 1000

list=[]
for _ in range(list_size):
    list.append(random.randint(0, 100))
"""
################# sequentialSearch ##############
"""
print("Sequential Search: ")
print(sequentialSearch(list, 50))
"""

################# binary search test ##############
"""
print(" binary search : ")
print(binSearch(list, 50))
"""
