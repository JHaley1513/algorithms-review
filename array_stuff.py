# Array util functions
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
