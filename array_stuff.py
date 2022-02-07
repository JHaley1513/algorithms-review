# Array util functions
import random
import string

def array_check_type(arr, t):
    if type(t) == list:
        for i in range(len(arr)):
            if type(arr[i]) not in t:
                print(f'arr[{i}] = {arr[i]}. type is {type(arr[i])}, which is not in [{array_str(t)}].')
    else:
        for i in range(len(arr)):
            if arr[i] != t:
                print(f'arr[{i}] = {arr[i]}. type is {type(arr[i])}, which is not {t}.')

def array_str(arr):
    for i in range(len(arr)):
        arr[i] = str(arr[i])
    return ', '.join(arr)
    # This way doesn't work for some reason
    # for i in arr:
    #     i = str(i)
    #     print(type(i))

def array_print(arr):
    for i in range(len(arr)):
        print(f'{arr[i]}', end='')
        if i < len(arr) - 1:
            print(', ', end='')
        else:
            print()
    # Sample output:
    # 1, 4, 7, 29, 31

def array_random(t='int', l=0):
    """Generate a random array of the selected type."""
    arr = []
    if l < 1 or l > 20:
        l = random.randint(5, 10)
    for i in range(l):
        if t == 'int':
            arr.append(random.randint(-50, 50))
        elif t == 'float':
            arr.append(round(random.uniform(-50.00, 50.00), 2))
        elif t == 'str':
            arr.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=N)))
        else:
            print(f'Unknown type for array_random: {t}')
            return []
    return arr

def array_int_input():
    """Take a user-defined number of numeric inputs, return an array of ints."""
    def int_in(msg=""):
        x = -1
        while True: # keep trying until receiving a valid input
            try:
                # Allows us to take a float string (i.e. '3.7') and convert it to an int (i.e. 3)
                x = int(float(input(msg)))
            except ValueError:
                print("Not a number, try again.")
            else: # NOT `finally`
                break
        return x

    n = int_in("Number of integers to enter: ")

    # Append new items to dynamically sized array, more Pythonic but less efficient
    arr = []
    for e in range(n):
        arr.append(int_in())
    return arr

    # Initialize array with predetermined number of items (non-dynamic array, for non-Python languages)
    # arr = [None] * n
    # for e in range(n):
        # arr[e] = int_in()