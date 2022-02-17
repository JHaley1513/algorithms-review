import array_utils
import tree_utils

class Thing:
    def __str__(self):
        return "Thing"
    def __repr__(self):
        return "Thing() object"


def t_array_str():
    a = [
        [1, 4, -99, 240.0],
        [' what\'s', '    ', ' up'],
        [83429, 'ok ', -3900322340.0],
        [False, True, False, Thing()],
    ]
    errors = 0
    print('Testing array_str...')

    for i in a:
        s = array_utils.array_str(i)
        if type(s) != str:
            print(f'array_str({i}) failed, returned {type(s)}')
            errors += 1
    print(f't_array_str finished with {errors} error(s).')
    print()


def t_array_print():
    a = [
        [1, 4, -99, 240.0],
        [' what\'s', '    ', ' up   '],
        [83429, 'ok ', -3900322340.0],
        [False, True, False, Thing()],
    ]
    # Expected outputs
    e = [
        '1, 4, -99, 240.0',
        ' what\'s,     ,  up   ',
        '83429, ok , -3900322340.0',
        'False, True, False, Thing'
    ]
    print('Testing array_print...')
    if len(a) != len(e):
        print(f'Arrays a and e have incompatible lengths: {len(a)} and {len(e)}.')
        return
    print('Expected vs result:')
    for i in range(len(a)):
        print(e[i])
        array_utils.array_print(a[i])
    print()
    

def t_array_random():
    print('Testing array_random...')
    array_utils.array_print(array_utils.array_random(int, 10))
    array_utils.array_print(array_utils.array_random(float, 8))
    array_utils.array_print(array_utils.array_random(str, 5))
    print()


def t_array_check_type():
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
        if array_utils.array_check_type(a[i], t[i]) != expected_output[i]:
            print(f'Incorrect result for array_check_type({a[i]}, {t[i]}), should be {expected_output[i]}.')
            errors += 1

    print(f't_array_check_type finished with {errors} error(s).')
    print()


def t_array_int_input():
    a = array_utils.array_int_input()
    print(f'{len(a)} ints inputted.')
    array_utils.array_print(a)


def t_array_max_digits():
    a = [
        [1, 10, 94, 0, 2],
        [940, 1, 8, 104, -6, -65],
        [-95, 40, 83, 12, 5]
    ]
    expected = [2, 3, 3]
    errors = 0
    for i in range(len(a)):
        m = array_utils.array_max_digits(a[i])
        e = expected[i]
        if m != e:
            print(f'Wrong max digits detected for a[{i}]: {m}, expected {e}')
            errors += 1
    print(f't_array_max_digits finished with {errors} error(s).')


if __name__=='__main__':
    # t_array_str()
    # t_array_print()
    # t_array_random()
    # t_array_check_type()
    # t_array_int_input()
    t_array_max_digits()
    print('test_algo_utils complete.')