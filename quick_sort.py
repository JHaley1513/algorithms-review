# Quicksort Θ(nlogn) expected, Θ(n2) worst case.
# Sorts in place.
# Similar to merge sort, you divide -> conquer -> recombine.
# Unlike merge sort, you divide between a smaller half and larger half,
# so once these are sorted you're already done
# - no need to "shuffle the two halves of the deck together" when recombining.

# We partition the array arr[p:r] into arr1[p:q] and arr2[q:r], such that every arr1[i] <= arr2[j].
# We also find index q to partition on.
# Then we sort arr1 and arr2 recursively until both sides (and therefore the whole array) have been sorted.
import algo_utils as algu


def partition(arr, p, r):
    """Operate on arr from p to r (exclusive, so from items p to r - 1)."""
    x = arr[p]
    i = p
    j = r - 1
    while True:
        # Decrease j and increase i until arr[i] ≥ x ≥ arr[j].
        # while arr[i] < x and i < r:
        while arr[i] < x:
            i += 1
        # while arr[j] > x and j >= p:
        while arr[j] > x:
            j -= 1
        if arr[i] == arr[j]:
            if i < r:
                i += 1
            elif j >= p:
                j += 1
            else:
                return i # or j
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else: # i has passed j. All items to the left of i > all items to the right of j, so we're done.
            return j

# x = 3 (val not idx)
# 3 3 2 1 4 (vals)
# i = 0, j = 4 (idx's)
# 1 3 2 3 4
# i = 0, j = 3
# 1 3 2 3 4
# i = 1, j = 3


def quick_sort(arr, p, r):
    print(f'[{algu.array_str(arr)}], p: {p}, r: {r}')
    if p < r:
        q = partition(arr, p, r)
        print(f'q: {q}')
        quick_sort(arr, p, q)
        # quick_sort(arr, p, q - 1)
        quick_sort(arr, q, r)


if __name__=='__main__':
    a = [5, 3, 2, 6, 4, 1, 3, 7]
    algu.array_print(a)
    quick_sort(a, 0, len(a))
    algu.array_print(a)