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


def tree_parent(node):
    return node // 2


def tree_left_child(tree, node):
    """
    @param tree: array of nodes making up a binary tree.
    @param node: index of the node we're finding the left child of.
    @return: index of the left child node, or 0 if it doesn't exist.
        (index 0 in a tree must be the top-level node and thus not a child, so 0 also denotes an invalid child).
    """
    child = (2 * node) + 1
    if child >= len(tree):
        # print(f'tree_left_child: the node at index {node} has no children.')
        return 0
    return child


def tree_right_child(tree, node):
    child = (2 * node) + 2
    if child >= len(tree):
        # print(f'tree_right_child: the node at index {node} has no right child.')
        return 0
    return child