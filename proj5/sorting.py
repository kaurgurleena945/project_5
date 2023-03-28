def bubble_sort(arr): 
    n = len(arr) # number of values in list
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): #0, n-1 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(items):
    n=len(items)
    for out in range(1,n):	#outer loop
        temp=items[out]	#select key/pivot
        i=out
        while i>0 and items[i-1]>temp:
            items[i]=items[i-1] #shift key
            i=i-1
        items[i]=temp #insertion


def selection_sort(items):
    n=len(items)
    for out in range(n-1):  # outer loop
        #find minimum between out+1 and n-1
        imin=out
        for i in range(out+1,n):	#inner loop
            if items[i]<items[imin]:
                imin=i #update	minimum index
                #swap
        items[out],items[imin]=items[imin],items[out]
        
'''
#################### Bubble Sort Test ######################

print("Bubble Sort Test: ")
list1 = [8, 2, 6, 9, 1]
print(list1)
bubble_sort(list1)
print(list1)

a=[4,5,1,7,2,3,6]
print(a)
bubble_sort(a)
print(a)

################# Insertion Sort Test ##################
print("\nInsertion Sort Test: ")
list1 = [8, 2, 6, 9, 1]
print(list1)
insertion_sort(list1)
print(list1)

a=[4,5,1,7,2,3,6]
print(a)
insertion_sort(a)
print(a)

################# Selection Sort Test ##################
print("\nSelection Sort Test: ")
list1 = [8, 2, 6, 9, 1]
print(list1)
selection_sort(list1)
print(list1)

a=[4,5,1,7,2,3,6]
print(a)
selection_sort(a)
print(a)
'''
