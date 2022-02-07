# Merge sort 
# Merge sort 1: pass full list each time, changing the left & right limits of what you operate on. (in-place sorting)
# Merge sort 2: pass partial list each time (not in-place)
from array_stuff import array_random, array_print

def merge1(arr, l, m, r):
    # left position <= mid < right.
    # we assume arr[l:d] and arr[m + 1:r] are already sorted, then merge to create arr[l:r].
    # num elements merged: r - l.
    print(f'merge1({l}, {m}, {r})')

    print('\t', end='')
    array_print(arr)
    i = k = l
    j = m
    # We're going through arr[l:m] using i, and arr[m:r] using j.
    # We go from l to r using index k, with every arr[k] becoming min(arr[i], arr[j]).
    while k < r and i < j:
        print(f'i={i}, j={j}, k={k}, {arr[i]}, {arr[j]}')
        # k becomes min(arr[i], arr[j])
        if arr[i] < arr[j]:
            arr[k], arr[i] = arr[i], arr[j]
            i += 1
        else:
            arr[k], arr[j] = arr[j], arr[i]
            j += 1
        k += 1
    print('\t', end='')
    array_print(arr)


def merge_sort1(arr, l, r):
    # the textbook starts from 1 and operates up to r inclusive, so 1...r.
    # we'll do it from 0 and exclusive, so 0...r.
    print(f'merge_sort1({l}, {r})')
    if l >= r - 1: # i.e. if l = 0 and r = 1, we're only looking at arr[0], so return.
        print('return')
        return
    m = (l + r) // 2
    merge_sort1(arr, l, m)
    merge_sort1(arr, m, r)
    merge1(arr, l, m, r)


def merge2(arr, sub_arr1, sub_arr2):
    """Merge two sorted subarrays into one combined sorted array."""
    i = j = 0 # index in sub_arr1 and sub_arr2
    while i + j < len(arr):
        # This way you'll usually end up with `list index out of range`
        if sub_arr1[i] < sub_arr2[j]:
            arr[i + j] = sub_arr1[i]
            i += 1
        else:
            arr[i + j] = sub_arr2[j]
            j += 1
        array_print(arr)


def merge_sort2(arr):
    n = len(arr)
    if n < 2:
        return
    mid = n // 2

    arr1 = arr[:mid]
    arr2 = arr[mid:n]
    merge_sort2(arr1)
    merge_sort2(arr2)

    l1 = len(arr1)
    l2 = len(arr2)
    # Best case A: largest in arr1 is smaller than smallest in arr2, so all of arr1 items < all of arr2 items
    if arr1[-1] < arr2[0]:
        for i in range(l1):
            arr[i] = arr1[i]
        for i in range(l2):
            arr[l1 + i] = arr2[i]
    # Best case B: all of arr1 items > all of arr2 items
    elif arr1[0] > arr2[-1]:
        for i in range(l2):
            arr[i] = arr2[i]
        for i in range(l1):
            arr[l2 + i] = arr1[i]
    # Normal case
    else:
        merge2(arr, arr1, arr2)

if __name__=='__main__':
    a = array_random()
    array_print(a)
    try:
        merge_sort2(a)
    finally:
        array_print(a)