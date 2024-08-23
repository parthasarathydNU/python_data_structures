from typing import Optional

class MinHeap:

    def __init__(self, ):
        self._heap = []

    def __str__(self, ):
        return "[" + ", ".join(map(str, self._heap)) + "]"



    def _left_child(self, index: int) -> Optional[int]:
        """
        This function returns the left child of the node at this index
        the left child is at 2*i + 1th index
        return None if does not exist
        """
        # print(f"Left child of index {index}")
        leftChildIndex = 2 * index + 1
        # print(f"LeftChild Index {leftChildIndex}")
        if leftChildIndex >= len(self._heap):
                return None

        return leftChildIndex

    def _right_child(self, index: int) -> Optional[int]:
        """
        This function returns the right child of the node at this index
        the right child is at 2*i + 2nd index
        return None if does not exist
        """
        rightChildIndex = 2 * index + 2
        if rightChildIndex >= len(self._heap):
                return None

        return rightChildIndex

    def _parent(self, index: int) -> Optional[int]:
        """
        This function returns the node at the parent index of this index
        """
        # print(f"Heap {self._heap}")
        # print(f"Parent index of {index}")
        if index == 0:
                return None
        parentIndex = (index-1) // 2
        return parentIndex

    def _heapify_up(self, index: int):
        """
        This function bubbles up the node to it's right spot
        """
        temp = index
        while temp != 0 and self._heap[self._parent(temp)] > self._heap[temp]:
            self._heap[self._parent(temp)], self._heap[temp] = self._heap[temp], self._heap[self._parent(temp)]
            temp = self._parent(temp)

    def insert(self, num: int):
        self._heap.append(num)
        self._heapify_up(len(self._heap) - 1)

    def _heapify_down(self, index):
        """
        This method takes the node at the current index and moves it down to the right
        Location in the array
        We always compare it with it's smallest child
        """
        
        smallest = index
        left_child = self._left_child(index)
        right_child = self._right_child(index)
        
        # Compare with left child
        if left_child is not None and self._heap[left_child] < self._heap[smallest]:
            smallest = left_child
        
        # Compare with right child
        if right_child is not None and self._heap[right_child] < self._heap[smallest]:
            smallest = right_child
        
        # If smallest is not the current index, swap and continue heapifying
        if smallest != index:
            self._heap[index], self._heap[smallest] = self._heap[smallest], self._heap[index]
            self._heapify_down(smallest)


    def extract_min(self):
        """
        Remove and return the minimum element from the heap
        Move the last element of the heap to the root
        call the _heapify_down method
        """
        if not self._heap:
            raise IndexError("Heap is empty")
        
        if len(self._heap) == 1:
            return self._heap.pop()
        
        min_val = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._heapify_down(0)
        
        return min_val
