def reverse_selection_sort(items):
    


########   Test code ##############
"""print("\nSelection Sort Test: ")
list1 = [8, 2, 6, 9, 1]
print(list1)
reverse_selection_sort(list1)
print(list1)

a=[4,5,1,7,2,3,6]
print(a)
reverse_selection_sort(a)
print(a) """

    

from sorting import selection_sort, bubble_sort, insertion_sort
import random
import time


list_sizes = [1000,2000,4000, 8000]
for size in list_sizes:

    list_insertion = []
    for x in range(size):
        list_insertion.append(random.randint(1,size/2))

    reverse_selection_sort(list_insertion)
    
    list_selection = list(list_insertion)
#    print(list_selection)
    list_bubble = list(list_insertion)
    selection_sort_start_time = time.time()
    selection_sort(list_selection)
    selection_sort_end_time = time.time()
    print("Time taken by selection sort is = %.6f"%(selection_sort_end_time-selection_sort_start_time))

    insertion_sort_start_time = time.time()
    insertion_sort(list_insertion)
    insertion_sort_end_time = time.time()
    print("Time taken by insertion sort is = %.6f"%(insertion_sort_end_time-insertion_sort_start_time))

    bubble_sort_start_time = time.time()
    bubble_sort(list_bubble)
    bubble_sort_end_time = time.time()
    print("Time taken by bubble sort is = %.6f"%(bubble_sort_end_time-bubble_sort_start_time))

    print("\n")

