from minHeap import MinHeap

def test_min_heap():
    heap = MinHeap()

    # Test case 1
    heap.insert(5)
    print("Test 1:", "Pass" if str(heap) == "[5]" else "Fail")

    # Test case 2
    heap.insert(3)
    print("Test 2:", "Pass" if str(heap) == "[3, 5]" else "Fail")

    # Test case 3
    heap.insert(7)
    print("Test 3:", "Pass" if str(heap) == "[3, 5, 7]" else "Fail")

    # Test case 4
    heap.insert(1)
    print("Test 4:", "Pass" if str(heap) == "[1, 3, 7, 5]" else "Fail")

    # Test case 5
    heap.insert(2)
    print("Test 5:", "Pass" if str(heap) == "[1, 2, 7, 5, 3]" else "Fail")

    # Test case 6
    heap.insert(6)
    print("Test 6:", "Pass" if str(heap) == "[1, 2, 6, 5, 3, 7]" else "Fail")

    # Test case 7
    heap.insert(4)
    print("Test 7:", "Pass" if str(heap) == "[1, 2, 4, 5, 3, 7, 6]" else "Fail")

# Run the tests
test_min_heap()

def test_min_heap_extract():
    heap = MinHeap()
    
    # Insert elements
    for element in [4, 8, 2, 5, 1, 6, 3, 7]:
        heap.insert(element)
    
    # Extract elements
    extracted = []
    for _ in range(8):
        extracted.append(heap.extract_min())

    # print(f"Extracted {extracted}")
    
    print("Extract min test:", "Pass" if extracted == [1, 2, 3, 4, 5, 6, 7, 8] else "Fail")

    # Test extracting from an empty heap
    try:
        heap.extract_min()
        print("Empty heap test: Fail")
    except IndexError:
        print("Empty heap test: Pass")

# Run the tests
test_min_heap_extract()
