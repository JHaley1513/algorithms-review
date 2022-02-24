import algo_utils as algu

def heapify(tree, node):
    """
    @param tree: array of integers, which are binary tree nodes.
    @param node: index of a node.
        We take the sub-tree rooted at this node and turn it into a binary heap
        (where every node's value ≤ its parent's value).
    @return: no return value, this operation is done in-place on the tree array.
    @runtime: O(logn) on n nodes, or O(h) for tree height h.
    """
    # These return the index of each child if it exists, or 0 if it doesn't.
    #   (index 0 in a tree must be the top-level node and thus not a child, so 0 also denotes an invalid child).
    l = algu.tree_left_child(tree, node)
    r = algu.tree_right_child(tree, node)
    largest = 0

    if l and tree[l] > tree[node]: # if left child exists and it's greater than its parent node
        largest = l
    else:
        largest = node

    if r and tree[r] > tree[largest]: # if right child exists and it's greater than max(parent, parent's left child)
        largest = r 

    if largest != node:
        tree[node], tree[largest] = tree[largest], tree[node] 
        heapify(tree, largest)


def heap_build(tree):
    for i in range((len(tree) // 2) - 1, -1, -1):
        heapify(tree, i)


def heap_sort(arr):
    algu.array_print(arr)
    heap_build(arr)
    algu.array_print(arr)
    # heap_size = len(arr)

    # heapify places the largest item at arr[0].
    # On every iteration, we move this item to the back of the array, and run heapify once more on the remaining items.
    for i in range(len(arr) - 1, 0, -1):
        print(arr[0])
        arr[0], arr[i] = arr[i], arr[0]
        # print(arr[0])
        # heap_size -= 1
        # heapify(arr[:heap_size], 0)
        heapify(arr[:i], 0)


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
    # heap_print([360, 340, 300, 280, 270, 190, 130, 120, 40, 1])

    # Should print:
    #   [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    # t = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    # heap_build(t)
    # algu.array_print(t)

    # Should print:
    #   [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    # t = [4, 1, 3, 2, 16, 9, 10, 14, 7, 8]
    # heap_build(t)
    # algu.array_print(t)

    # Should print:
    #   [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
    t = [5, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    heap_sort(t)
    algu.array_print(t)

    # Currently VERY incorrect output:
    # Initial array:                5, 4, 10, 14, 7, 9, 3, 2, 8, 1
    # heap sort on range(9, 9, -1): 5, 4, 10, 14, 7, 9, 3, 2, 8, 1
    # heap sort on range(9, 8, -1): 1, 4, 10, 14, 7, 9, 3, 2, 8, 5
    # heap sort on range(9, 7, -1): 8, 4, 10, 14, 7, 9, 3, 2, 5, 1
    # heap sort on range(9, 6, -1): 2, 4, 10, 14, 7, 9, 3, 5, 1, 8
    # heap sort on range(9, 5, -1): 3, 4, 10, 14, 8, 9, 5, 1, 7, 2
    # heap sort on range(9, 4, -1): 9, 4, 10, 14, 8, 5, 1, 7, 2, 3
    # heap sort on range(9, 3, -1): 8, 4, 10, 14, 5, 1, 7, 2, 3, 9
    # heap sort on range(9, 2, -1): 14, 4, 10, 9, 1, 7, 2, 3, 5, 8
    # Literally every single one is just the first item (5) swapping with whatever item's at the end of the specified range, at least until the last one.
    # It should actually be constructing a heap before sorting (so 5 shouldn't be the first item when starting out, ever), but that doesn't seem to be happening.