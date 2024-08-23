# Data Structures and Algorithms Implementation

This project contains implementations of various data structures and algorithms, organized into separate modules.

## Modules

### Graph

The `graph` directory contains implementations related to graph data structures and algorithms.

- `graph.py`: Contains the main Graph class implementation with various graph algorithms.
- `graphTest.py`: Unit tests for the Graph class and its methods.
- `performanceTest.py`: Performance tests, particularly for Dijkstra's algorithm.
- `Readme.md`: Detailed documentation about the Graph implementation and performance analysis.

### MinHeap

The `minHeap` directory contains an implementation of a Min Heap data structure.

- `minHeap.py`: Contains the MinHeap class implementation.
- `tests.py`: Primary unit tests for the MinHeap class.
- `test2.py`: Additional tests or alternative test implementations for the MinHeap.

## Usage

To use these implementations in your project:

1. Clone this repository.
2. Import the desired classes from the respective modules.

Example:

```python
from graph.graph import Graph
from minHeap.minHeap import MinHeap

# Use the Graph class
g = Graph()
g.add_edge(0, 1)

# Use the MinHeap class
heap = MinHeap()
heap.insert(5)
```

## Testing

Each module contains its own test files. To run the tests:

1. Navigate to the specific module directory.
2. Run the test files using Python.

Example:

```bash
cd graph
python graphTest.py

cd ../minHeap
python tests.py
python test2.py
```

## Documentation

For detailed information about each implementation:

- Refer to the `Readme.md` file in the `graph` directory for comprehensive documentation on the Graph implementation and its performance characteristics.
- Check the comments and docstrings within each `.py` file for specific details about classes and methods.

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues for any bugs or enhancements.
