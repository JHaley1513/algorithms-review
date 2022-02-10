from array_stuff import *

def t_array_check_type():
    class Thing: pass

    a = [
        [1, 0, -9, 24],
        [4.50, -9.8, 6.5],
        ['x', 'xyz', 'boom'],
        [2, 4.05, 4, -60.8, 7.9],
        ['three', 'five', 23248, 4.0],
        [['four', 4, 4.0], 'ok', 2700, -498.56, False],
        [2560, True, Thing()]
    ]
    t = [int, float, str, [int], [int, float, str, bool], [list, str, int, float, bool], [bool, Thing]]

    if len(a) != len(t):
        print(f'Arrays a and t have incompatible lengths: {len(a)} and {len(t)}.')
        return
    for i in range(len(a)):
        print(array_check_type(a[i], t[i])) # if False, will print `Incorrect Type: ...` then `False`.
    
    # Expected output:
    # True True



if __name__=='__main__':
    t_array_check_type()
    # array_int_input() # take user input
    # print()