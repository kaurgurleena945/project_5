def modifiedbinSearch(mylist, x):
    
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


ex_list_1 = [3,3,3,3,5,5,5,6,7,7,7,8,8,10,10]
ex_list_2 = [7,7,7,45,45,32,65,65,444,444,2,2,2,2,9]

print(modifiedbinSearch(ex_list_1, 5)) # should be 4
print(modifiedbinSearch(ex_list_2, 45) # should be 3
