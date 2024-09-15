from RedBlack import RedBlackTree

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + f'-> {node.value} ({node.color})')
        print_tree(node.left, level + 1)

def is_red_black_tree_valid(tree):
    def is_valid(node):
        if node is None:
            return 1  # Height of a black null node is 1

        left_height = is_valid(node.left)
        right_height = is_valid(node.right)

        if left_height == 0 or right_height == 0:
            return 0  # Invalid

        if left_height != right_height:
            return 0  # Invalid

        if node.color == "Red" and (
            (node.left and node.left.color == "Red") or
            (node.right and node.right.color == "Red")
        ):
            return 0  # Invalid

        return left_height + (1 if node.color == "Black" else 0)

    root_black = is_valid(tree.root)
    return root_black > 0 and tree.root.color == "Black"

def test_red_black_tree():
    # Test 1: Ascending order insertion
    print("Test 1: Ascending order insertion")
    rbt_balanced = RedBlackTree()
    rbt_unbalanced = RedBlackTree()
    for i in range(1, 8):
        rbt_balanced.insertNode(i, balance=True)
        rbt_unbalanced.insertNode(i, balance=False)
    
    print("Balanced:")
    print_tree(rbt_balanced.root)
    print("Is valid Red-Black Tree:", is_red_black_tree_valid(rbt_balanced))
    
    print("\nUnbalanced:")
    print_tree(rbt_unbalanced.root)
    print("Is valid Red-Black Tree:", is_red_black_tree_valid(rbt_unbalanced))

    # Test 2: Descending order insertion
    print("\nTest 2: Descending order insertion")
    rbt_balanced = RedBlackTree()
    rbt_unbalanced = RedBlackTree()
    for i in range(7, 0, -1):
        rbt_balanced.insertNode(i, balance=True)
        rbt_unbalanced.insertNode(i, balance=False)
    
    print("Balanced:")
    print_tree(rbt_balanced.root)
    print("Is valid Red-Black Tree:", is_red_black_tree_valid(rbt_balanced))
    
    print("\nUnbalanced:")
    print_tree(rbt_unbalanced.root)
    print("Is valid Red-Black Tree:", is_red_black_tree_valid(rbt_unbalanced))

    # Test 3: Random order insertion
    print("\nTest 3: Random order insertion")
    rbt_balanced = RedBlackTree()
    rbt_unbalanced = RedBlackTree()
    for i in [4, 2, 6, 1, 3, 5, 7]:
        rbt_balanced.insertNode(i, balance=True)
        rbt_unbalanced.insertNode(i, balance=False)
    
    print("Balanced:")
    print_tree(rbt_balanced.root)
    print("Is valid Red-Black Tree:", is_red_black_tree_valid(rbt_balanced))
    
    print("\nUnbalanced:")
    print_tree(rbt_unbalanced.root)
    print("Is valid Red-Black Tree:", is_red_black_tree_valid(rbt_unbalanced))

    # Test 4: Duplicate values
    print("\nTest 4: Duplicate values")
    rbt_balanced = RedBlackTree()
    for i in [3, 1, 5, 1, 2, 3, 4, 5]:
        rbt_balanced.insertNode(i, balance=True)
    
    print("Balanced:")
    print_tree(rbt_balanced.root)
    print("Is valid Red-Black Tree:", is_red_black_tree_valid(rbt_balanced))

test_red_black_tree()
