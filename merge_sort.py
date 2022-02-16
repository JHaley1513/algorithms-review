# Merge sort O(nlogn)
# Merge sort 1: pass full list each time, changing the left & right limits of what you operate on. (in-place sorting)
# Merge sort 2: pass partial list each time (not in-place)
# import algorithms-review.algo_utils as algu
import algo_utils as algu

def merge1(arr, l, m, r):
    # Left position <= mid < right.
    # We assume arr[l:d] and arr[m + 1:r] are already sorted, then merge to create arr[l:r].
    # Num elements merged: r - l.
    i = l
    j = m

    # arr[i] is the smallest item in the range i...j not inclusive.
    # arr[j] is the smallest item in the range j...r.
    # On every iteration, after comparing the two, arr[i] should become the smallest remaining item.
    # If i == j or j reaches r, we're done sorting (if any items remain, they just go at the end of the array in their current ordering).
    # Else if arr[i] <= arr[j] and i < j, increment i.
    # Else (if arr[i] > arr[j]), put arr[j] in arr[i]'s place and shift all items between i and j to the right.
    while i < j and j < r:
        if arr[i] <= arr[j]:
            # arr[i] is already the smallest remaining item.
            i += 1
        else:
            # Shift all items between i and j to the right, to make room for the new arr[i].
            temp = arr[j]
            for x in range(j, i, -1): 
                arr[j] = arr[j-1]
            arr[i] = temp
            i += 1
            j += 1
            

def merge_sort1(arr, l, r):
    # The textbook starts from 1 and operates up to r inclusive, so 1...r.
    # We'll do it from 0 and exclusive, so 0...r.
    if l >= r - 1: # i.e. if l = 0 and r = 1, we're only looking at arr[0], so return.
        return
    m = (l + r) // 2
    merge_sort1(arr, l, m)
    merge_sort1(arr, m, r)
    merge1(arr, l, m, r)


def merge2(arr, sub_arr1, sub_arr2):
    """Merge two sorted subarrays into one combined sorted array."""
    i = j = 0 # index in sub_arr1 and sub_arr2
    while i + j < len(arr):
        if j == len(sub_arr2) or (i < len(sub_arr1) and sub_arr1[i] < sub_arr2[j]):
            arr[i + j] = sub_arr1[i]
            i += 1
        else:
            arr[i + j] = sub_arr2[j]
            j += 1


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
    if arr1[-1] <= arr2[0]:
        for i in range(l1):
            arr[i] = arr1[i]
        for i in range(l2):
            arr[l1 + i] = arr2[i]
    # Best case B: all of arr1 items > all of arr2 items
    elif arr1[0] >= arr2[-1]:
        for i in range(l2):
            arr[i] = arr2[i]
        for i in range(l1):
            arr[l2 + i] = arr1[i]
    # Normal case
    else:
        merge2(arr, arr1, arr2)


if __name__=='__main__':
    merge_type = 1
    a = algu.array_random()

    if algu.array_check_type(a, int):
        algu.array_print(a)

        if merge_type == 1:
            merge_sort1(a, 0, len(a))
        elif merge_type == 2:
            merge_sort2(a)
        else:
            print(f'Unknown merge type: {merge_type}')

        algu.array_print(a)