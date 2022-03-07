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
        # This is the crucial if-statement, without it we loop forever.
        if arr[i] == arr[j]:
            if i < r:
                i += 1
            # Interestingly, we don't need an `elif j > p` block.
            # However, if we remove the `if i < r: i++` and replace it with `if j > p: j--`,
            # the algorithm doesn't work.
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else: # i has passed j. All items to the left of i > all items to the right of j, so we're done.
            return j


def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q)
        quick_sort(arr, q + 1, r)


if __name__=='__main__':
    trials = 7
    errors = 0

    for i in range(trials):
        a = algu.array_random()
        print(f'Before sorting: {algu.array_str(a)}')
        quick_sort(a, 0, len(a))
        print(f'After sorting:  {algu.array_str(a)}')
        s = algu.array_is_sorted(a)
        if not s:
            print("NOT sorted.")
            errors += 1
        print()

    print(f'Quicksort on {trials} arrays returned {errors} errors.')
