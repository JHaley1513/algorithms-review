def tree_prev_power_2(x):
    """Find n, the largest power of 2 such that 2^n ≤ x.
    Returns -1 meaning undefined for x < 1.
    """
    if type(x) != int:
        x = int(x)
        print(f'prev_power_2: Casting x to {x}.')
    if x < 1:
        print(f'prev_power_2: Undefined behavior for x < 1.')
        return -1
    if x == 1: return 0
    n = 1
    while 2 ** (n + 1) <= x:
        n += 1
    return n


def tree_next_power_2(x):
    """Find n, the smallest power of 2 such that 2^n ≥ x."""
    if type(x) != int:
        x = int(x)
        print(f'next_power_2: casting x to {x}.')
    if x < 2: return 0
    if x == 2: return 1
    n = 1
    while 2 ** n < x:
        n += 1
    return n