def heap_print(a):
    """Takes an array of binary heap nodes and prints them as a binary tree."""
    # Some definitions:
    # a = input array, n = number of nodes (aka len(a)), h = height of tree, w = width of tree.
    # m before a variable name means the maximum possible value for it for the current tree height.
    # 
    # There's a few main steps:
    # Determine tree height h.
    #   h is the nearest power of 2 greater than or equal to n.
    #   In other words, 2^h >= n, 2^(h - 1) < n.
    # Determine maximum tree width (number of possible child nodes at the bottom-most level)
    #   maximum width mw = 2^(h - 1).
    #   Also, the bottom level's max number of nodes is exactly the total of all other levels plus 1.
    # Determine how many digits each node contains (and whether the node is a negative number).
    #   For simplicity's sake, we're restricting nodes to the values -99 ≤ v ≤ 999.

    # We first find the maximum power


def prev_power_2(x):
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



def next_power_2(x):
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


if __name__=='__main__':
    for i in range(0, 20):
        print(f'{i}≥2^{prev_power_2(i)}')
        # print(f'{i}≤2^{next_power_2(i)}')