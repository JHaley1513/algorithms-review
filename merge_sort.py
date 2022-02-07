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


# def merge2(arr, l, m, r):

# def merge_sort2(arr, l, r):

if __name__=='__main__':
    a = array_random()
    array_print(a)
    try:
        merge_sort1(a, 0, len(a))
    finally:
        array_print(a)