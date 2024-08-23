from minHeap import MinHeap

# Test cases	

# heap = MinHeap()
# print(heap)

# heap._heap = [1, 3, 5, 7, 9]
# print(heap)  # Should print: [1, 3, 5, 7, 9]

# # Test cases
# heap = MinHeap()
# heap.insert(5)
# heap.insert(3)
# heap.insert(7)
# print(heap)  # Should print: [5, 3, 7]

# heap.insert(1)
# heap.insert(9)
# print(heap)  # Should print: [5, 3, 7, 1, 9]


# Test cases
# heap = MinHeap()
# heap._heap = [1, 2, 3, 4, 5, 6, 7]  # Simulating a heap for testing

# print(heap)

# print(heap._parent(0))  # Should print: None
# print(heap._parent(1))  # Should print: 0
# print(heap._parent(3))  # Should print: 1

# print(heap._left_child(1))  # Should print: 3
# print(heap._right_child(1))  # Should print: 4

# print(heap._left_child(3))  # Should print: 7
# print(heap._right_child(3))  # Should print: None

# print(heap._left_child(6))  # Should print: None
# print(heap._right_child(6))  # Should print: None

# First, let's create a MinHeap instance and populate it with some data
heap = MinHeap()
heap._heap = [1, 2, 3, 4, 5, 6, 7]  # Simulating a heap for testing

# Test cases for _parent method
print("Testing _parent method:")
print(heap._parent(0))  # Should print: None (root has no parent)
print(heap._parent(1))  # Should print: 0
print(heap._parent(2))  # Should print: 0
print(heap._parent(3))  # Should print: 1
print(heap._parent(4))  # Should print: 1
print(heap._parent(5))  # Should print: 2
print(heap._parent(6))  # Should print: 2

# Test cases for _left_child method
print("\nTesting _left_child method:")
print(heap._left_child(0))  # Should print: 1
print(heap._left_child(1))  # Should print: 3
print(heap._left_child(2))  # Should print: 5
print(heap._left_child(3))  # Should print: None
print(heap._left_child(4))  # Should print: None
print(heap._left_child(5))  # Should print: None
print(heap._left_child(6))  # Should print: None

# Test cases for _right_child method
print("\nTesting _right_child method:")
print(heap._right_child(0))  # Should print: 2
print(heap._right_child(1))  # Should print: 4
print(heap._right_child(2))  # Should print: 6
print(heap._right_child(3))  # Should print: None
print(heap._right_child(4))  # Should print: None
print(heap._right_child(5))  # Should print: None
print(heap._right_child(6))  # Should print: None

# Test with an index out of bounds
print("\nTesting with out of bounds index:")
print(heap._parent(7))       # Should print: 3
print(heap._left_child(7))   # Should print: None
print(heap._right_child(7))  # Should print: None
