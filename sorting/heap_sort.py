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


def next_power_2(x):
    """Find nearest power of 2 that's ≥ x."""
    if x <= 1: return 0
    if x <= 2: return 1
    n = 1
    while n < x:
        n *= 2
    return n


if __name__=='__main__':
    for i in range(20):
        print(f'{next_power_2(i)} ', end='')