# Insertion sort O(n^2)
from array_stuff import array_int_input

def insertion_sort():
    arr = array_int_input()

    for j in range(1, len(arr)): # originally started range at 2, since the textbook starts indexing from 1 not 0
        key = arr[j]
        i = j - 1
        while i >= 0 and key < arr[i]: # originally was > 0 according to the book which is > -1 here, but I prefer >= 0 for clarity.
            arr[i + 1] = arr[i]
            i -= 1

    for i in range(len(arr)):
        print(f'{arr[i]}', end='')
        if i < len(arr) - 1:
            print(', ', end='')
        else:
            print()
            

if __name__=='__main__':
    insertion_sort()