from array_stuff import *

def t_array_check_type():
    class Thing: pass
    a = [
        [1, 0, -9, 24],
        [4.50, 'yes', 6.5],
        ['x', 'xyz', 'boom'],
        [2, 4.05, 4, -60.8, 7.9],
        ['three', 'five', 23248, 4.0],
        [['four', 4, 4.0], 'ok', 2700, -498.56, False],
        [2560, True, Thing()]
    ]
    t = [int, int, str, [int], [int, float, str, bool], [list, str, int, float, bool], [bool, Thing]] # Thing() works too

    # Expected output:
    # True, False (str), True, False (float), True, True, False (int)
    expected_output = [True, False, True, False, True, True, False]
    errors = 0

    print('Testing array_check_type...')

    if len(a) != len(t):
        print(f'Arrays a and t have incompatible lengths: {len(a)} and {len(t)}.')
        return
    elif len(a) != expected_output:
        print(f'Arrays a and expected_output have incompatible lengths: {len(a)} and {len(expected_output)}.')
    
    for i in range(len(a)):
        # print(array_check_type(a[i], t[i])) # if False, will print `Incorrect Type: ...` then `False`.
        if array_check_type(a[i], t[i]) != expected_output[i]:
            print(f'Incorrect result for array_check_type({a[i]}, {t[i]}), should be {expected_output[i]}.')
            errors += 1

    print(f'array_check_type: {errors} error(s).')
    print()


if __name__=='__main__':
    t_array_check_type()
    # array_int_input() # take user input