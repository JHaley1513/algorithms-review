import algo_utils as algu

def heapify(tree, node):
    """
    @param tree: array of integers, which are binary tree nodes.
    @param node: index of a node.
        We take the sub-tree rooted at this node and turn it into a binary heap
        (where every node's value ≤ its parent's value).
    @return: no return value, this operation is done in-place on the tree array.
    """
    l = algu.tree_left_child(tree, node)
    r = algu.tree_right_child(tree, node)
    largest = -1

    if l < len(tree) and tree[l] > tree[node]:
        largest = l
    else:
        largest = node

    if r < len(tree) and tree[r] > tree[largest]:
        largest = r 

    if largest != node:
        tree[i], tree[largest] = tree[largest], tree[i] 
        heapify(tree, largest)


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

    tree = []
    # We first find the maximum power
    
    # Number of potential bottom-level nodes is the highest power of 2 that's ≤ the total number of nodes.
    # i.e. a tree with height 4 can have 8 to 15 total nodes, 
    # which is 7 non-bottom nodes plus 1 to 8 bottom level nodes, so max_bottom would be 8.
    max_bottom = 2 ** (algu.prev_power_2(len(a)))
    # Then we find the max number of digits of all nodes in the row (- negative sign counts as a digit).
    # Then we allocate that many spaces plus one (for space between nodes) per node.
    
    # Iterate through bottom row.
    # There are always (max_bottom - 1) non-bottom nodes in a complete binary tree.
    # So, we start from the first bottom node and go to the end.
    bottom_nodes = a[max_bottom - 1:]
    max_digits = algu.array_max_digits(bottom_nodes)
    row = []
    for i in range(len(bottom_nodes)):
        row.append(str(bottom_nodes[i]))
        if i < len(bottom_nodes) - 1:
            # Add spaces between nodes, with extra spaces if the node isn't max_digits wide.
            spaces = 1 + max_digits - algu.num_digits(bottom_nodes[i])
            row.append(' ' * spaces)
        
    tree.append(''.join(row))
    print(tree[0])


if __name__=='__main__':
    heap_print([360, 340, 300, 280, 270, 190, 130, 120, 40, 1])