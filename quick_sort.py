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
        while arr[i] < x:
            i += 1
        while arr[j] > x:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else: # i has passed j. All items to the left of i > all items to the right of j, so we're done.
            print('return j')
            return j


def quick_sort(arr, p, r):
    if p < r - 1:
        q = partition(arr, p, r)
        print('passed partition')
        quick_sort(arr, p, q)
        quick_sort(arr, q, r)


if __name__=='__main__':
    a = [5, 3, 2, 6, 4, 1, 3, 7]
    algu.array_print(a)
    quick_sort(a, 0, len(a))
    algu.array_print(a)