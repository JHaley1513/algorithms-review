import algo_utils as algu

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
    
    # Number of potential bottom-level nodes is the highest power of 2 that's ≤ the total number of nodes.
    # i.e. a tree with height 4 can have 8 to 15 total nodes, 
    # which is 7 non-bottom nodes plus 1 to 8 bottom level nodes, so max_bottom would be 8.
    max_bottom = algu.tree_prev_power_2(a)

    # Then we find the max number of digits of all nodes in the row (- negative sign counts as a digit).
    # Then we allocate that many spaces plus one (for space between nodes) per node.
    
    # Iterate through bottom row.
    # There are always (max_bottom - 1) non-bottom nodes in a complete binary tree.
    # So, we start from the first bottom node and go to the end.
    

    for i in range(0, 4000, 70):
        print(f'')

if __name__=='__main__':
    pass