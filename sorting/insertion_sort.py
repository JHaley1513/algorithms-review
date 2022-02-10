# Insertion sort O(n^2)
from array_stuff import array_int_input, array_random, array_print
import argparse

def insertion_sort_simple():
    arr = array_random()
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and key < arr[i]: # key < arr[i] makes more sense to me than arr[i] > key (the way it's written in the book)
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    array_print(arr)


def insertion_sort(descending=False, random=False):
    if random:
        arr = array_random()
    else:
        arr = array_int_input()

    print('Input: ', end='')
    array_print(arr)

    if descending:
        print('Sorting from greatest to least...')
    else:
        print('Sorting from least to greatest...')

    for j in range(1, len(arr)): # originally started range at 2, since the textbook starts indexing from 1 not 0
        key = arr[j]
        i = j - 1
        if not descending: # sort list in order of ascending value (least to greatest)
            while i >= 0 and key < arr[i]: # originally was > 0 according to the book which is > -1 here, but I prefer >= 0 for clarity.
                arr[i + 1] = arr[i]
                i -= 1
        else: # descending (greatest to least). only difference is moving key to the left after key < arr[i] vs key > arr[i].
            while i >= 0 and key > arr[i]:
                arr[i + 1] = arr[i]
                i -= 1
        arr[i + 1] = key

    print('Output: ', end='')
    array_print(arr)


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Decide which version of insertion sort to use.')
    parser.add_argument('-d', '--descend', action='store_true', help='whether to sort in order of descending value. default: False')
    parser.add_argument('-r', '--random', action='store_true', help='whether to generate random values instead of taking user input. default: False')
    args = vars(parser.parse_args()) # dictionary of argname:value. (argname above is `descend` not `d`)

    insertion_sort(descending=args['descend'], random=args['random'])