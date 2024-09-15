from RedBlack import RedBlackTree

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + f'-> {node.value} ({node.color})')
        print_tree(node.left, level + 1)

def test_rbt_insertion():
    rbt = RedBlackTree()

    # Test 1: Single node insertion
    rbt.insertNode(10)
    print("Test 1: Single node insertion")
    print_tree(rbt.root)
    print("\n")

    # Test 2: Ascending order insertion
    rbt = RedBlackTree()
    for value in [1, 2, 3, 4, 5]:
        rbt.insertNode(value)
    print("Test 2: Ascending order insertion")
    print_tree(rbt.root)
    print("\n")

    # Test 3: Descending order insertion
    rbt = RedBlackTree()
    for value in [5, 4, 3, 2, 1]:
        rbt.insertNode(value)
    print("Test 3: Descending order insertion")
    print_tree(rbt.root)
    print("\n")

    # Test 4: Duplicate values
    rbt = RedBlackTree()
    for value in [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]:
        rbt.insertNode(value)
    print("Test 4: Duplicate values")
    print_tree(rbt.root)
    print("\n")

    # Test 5: Mixed insertion
    rbt = RedBlackTree()
    for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        rbt.insertNode(value)
    print("Test 5: Mixed insertion")
    print_tree(rbt.root)
    print("\n")

test_rbt_insertion()
