# Red Black Trees

## Whats a red or a black node?

- In a Red-Black Tree, every node is colored either red or black
- This coloring is a key part of maintaining the tree's balance

## Meaning of colors:
- Black nodes are used to ensure the tree remains balanced, they contribute to the "Black Height" of the tree
- Red nodes allow for some flexibility in the tree structure, but they come with restrictions in order to maintain balance

## Properties of Red Black Trees:
- The root node is always a black node
- All  leaf nodes (Null Nodes) are considered black nodes [ here do we mean that only the null nodes at the end are considered as leaf nodes ? And even the nodes that don't have children are considered as non-leaf nodes ]
    > Yes, in practical implementations, only the null (None in Python) values at the end of the tree are considered as the black leaf nodes. Nodes that contain values but don't have children are still internal nodes, not leaf nodes.

- If a node is red, both it's children must be black
- Every path from a node to it's descendant leaves must contain the same number of black nodes (this is called the "black height")

## Balancing Act: 
- The color rules help ensure that the longest path from the root to any leaf is no more than twice as long as the shortest path [How is this possible ?]
- this guarantess that the tree remains approximately balanced ensuring O(logn) time for basic operations

## Insertion and Deletion: 
- New nodes are always inserted as red. This is because adding a red node dosen't change the black height of any path
- If inserting a red node violates the Red-Black properties, we perform rotation and color changes to fix it

## Significance: 
- Being a black node, means the node contributes to the black height of the tree
- Being a red node, means the node provides structural flexibility without affecting the black height

In this implementation, we will be checking for vioations and be deciding how to fix them, we will be essentially ensuring that these color properties are maintained throughout the tree.

## Examples of trees without being balanced:

```
Test 1: Single node insertion
-> 10 (Black)


Test 2: Ascending order insertion
                -> 5 (Red)
            -> 4 (Red)
        -> 3 (Red)
    -> 2 (Red)
-> 1 (Black)


Test 3: Descending order insertion
-> 5 (Black)
    -> 4 (Red)
        -> 3 (Red)
            -> 2 (Red)
                -> 1 (Red)


Test 4: Duplicate values
            -> 9 (Red)
                -> 6 (Red)
        -> 5 (Red)
    -> 4 (Red)
-> 3 (Black)
        -> 2 (Red)
    -> 1 (Red)


Test 5: Mixed insertion
        -> 14 (Red)
            -> 13 (Red)
    -> 10 (Red)
-> 8 (Black)
            -> 7 (Red)
        -> 6 (Red)
            -> 4 (Red)
    -> 3 (Red)
        -> 1 (Red)

```

# Questions

## The color rules help ensure that the longest path from the root to any leaf is no more than twice as long as the shortest path. How is this possible ?
 
This is a key property of Red-Black Trees, and understanding it helps grasp why these trees maintain good balance. Let's break it down:

1. Black Height Property:
   - Every path from the root to a leaf (NIL node) must have the same number of black nodes. This is called the "black height" of the tree.

2. Red Node Restriction:
   - Red nodes cannot have red children. This means you can never have two red nodes in a row on any path.

3. Shortest Possible Path:
   - The shortest path would consist of all black nodes.
   - Let's say this path has a black height of h (h black nodes).

4. Longest Possible Path:
   - The longest path would alternate between red and black nodes, starting with black.
   - This path would look like: Black, Red, Black, Red, ..., Black
   - It would have h black nodes (to maintain the black height) and at most h-1 red nodes interspersed between them.

5. Length Comparison:
   - Shortest path length: h
   - Longest path length: 2h - 1 (h black + (h-1) red)

6. Conclusion:
   - The longest path (2h - 1) is always less than twice the length of the shortest path (2h).

This property ensures that the tree remains roughly balanced. Even in the worst case, no path is more than twice as long as any other path, which guarantees O(log n) time complexity for basic operations like search, insert, and delete.

Here's a simple example:
- Shortest path: B - B - B (length 3)
- Longest possible path: B - R - B - R - B (length 5)

In this case, the longest path (5) is less than twice the shortest path (3 * 2 = 6).

This balancing ensures that Red-Black Trees provide a good compromise between the perfect balance of AVL trees and the potentially more unbalanced structure of regular BSTs.

Does this explanation help clarify how the color rules maintain this balance property? Let me know if you'd like me to elaborate on any part of this.

```
Test 1: Ascending order insertion
Balanced:
            -> 7 (Red)
        -> 6 (Black)
            -> 5 (Red)
    -> 4 (Red)
        -> 3 (Black)
-> 2 (Black)
    -> 1 (Black)
Is valid Red-Black Tree: True

Unbalanced:
                        -> 7 (Red)
                    -> 6 (Red)
                -> 5 (Red)
            -> 4 (Red)
        -> 3 (Red)
    -> 2 (Red)
-> 1 (Black)
Is valid Red-Black Tree: False

Test 2: Descending order insertion
Balanced:
    -> 7 (Black)
-> 6 (Black)
        -> 5 (Black)
    -> 4 (Red)
            -> 3 (Red)
        -> 2 (Black)
            -> 1 (Red)
Is valid Red-Black Tree: True

Unbalanced:
-> 7 (Black)
    -> 6 (Red)
        -> 5 (Red)
            -> 4 (Red)
                -> 3 (Red)
                    -> 2 (Red)
                        -> 1 (Red)
Is valid Red-Black Tree: False

Test 3: Random order insertion
Balanced:
        -> 7 (Red)
    -> 6 (Black)
        -> 5 (Red)
-> 4 (Black)
        -> 3 (Red)
    -> 2 (Black)
        -> 1 (Red)
Is valid Red-Black Tree: True

Unbalanced:
        -> 7 (Red)
    -> 6 (Red)
        -> 5 (Red)
-> 4 (Black)
        -> 3 (Red)
    -> 2 (Red)
        -> 1 (Red)
Is valid Red-Black Tree: False

Test 4: Duplicate values
Balanced:
    -> 5 (Black)
        -> 4 (Red)
-> 3 (Black)
        -> 2 (Red)
    -> 1 (Black)
Is valid Red-Black Tree: True
```
