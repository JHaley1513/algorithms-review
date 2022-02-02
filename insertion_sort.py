# Insertion sort O(n^2)
from array_stuff import array_int_input, array_print, array_random

def insertion_sort(random=True):
    if random:
        arr = array_random()
    else:
        arr = array_int_input()

    print('Input: ', end='')
    array_print(arr)

    for j in range(1, len(arr)): # originally started range at 2, since the textbook starts indexing from 1 not 0
        key = arr[j]
        i = j - 1
        while i >= 0 and key < arr[i]: # originally was > 0 according to the book which is > -1 here, but I prefer >= 0 for clarity.
            arr[i + 1] = arr[i]
            i -= 1

    print('Output: ', end='')
    array_print(arr)
            

if __name__=='__main__':
    insertion_sort()