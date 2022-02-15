# Array util functions
import random
import string


def array_str(arr):
    """Returns an array as a comma-separated string with no brackets"""
    new = []
    for i in range(len(arr)):
        new.append(str(arr[i]))
    return ', '.join(new)


def array_print(arr, break_after=True):
    """Prints an array separated by commas with no brackets"""
    for i in range(len(arr)):
        print(f'{arr[i]}', end='')
        if i < len(arr) - 1:
            print(', ', end='')
    if break_after:
        print()
    # Sample output:
    # 1, 4, 7, 29, 31


def array_random(t=int, n=0):
    """Generate a random array of the selected type."""
    arr = []
    if n < 1 or n > 20:
        n = random.randint(5, 10)
    for i in range(n):
        if t == int:
            arr.append(random.randint(-50, 50))
        elif t == float:
            arr.append(round(random.uniform(-50.00, 50.00), 2))
        elif t == str:
            arr.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=10)))
        else:
            print(f'Unknown type for array_random: {t}')
            return []
    return arr


def array_check_type(arr, t):
    """Checks if arr's items are all type t, or all in t if t is a list of types."""
    if type(t) == list:
        for i in range(len(arr)):
            if type(arr[i]) not in t:
                print(f'array_check_type: expected [{array_str(t)}], but {arr[i]} is {type(arr[i])}.')
                return False
    else:
        for i in range(len(arr)):
            if type(arr[i]) != t:
                print(f'array_check_type: expected {t}, but {arr[i]} is {type(arr[i])}.')
                return False
    return True


def array_int_input():
    """Take a user-defined number of numeric inputs, return an array of ints."""
    def int_in(msg=""):
        x = -1
        while True: # keep trying until receiving a valid input
            try:
                # Take an int or float and convert it to an int (i.e. 3.7 becomes 3)
                x = int(float(input(msg)))
            except ValueError:
                print("Not a number, try again.")
            else: # once a valid input has been received, break and return
                break
        return x

    redo = True
    while redo:
        # If the user accidentally asks for too many inputs, they get a chance to redo it.
        n = int_in("Number of integers to enter: ")
        if n > 10:
            answer = input("Are you sure? [y]/n: ").strip().lower()
            if answer != 'n' and answer != 'no':
                redo = False
        else:
            redo = False
        
    arr = []
    for e in range(n):
        arr.append(int_in())
    return arr