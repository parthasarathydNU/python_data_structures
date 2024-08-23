# Graph Algorithms Implementation and Performance Analysis

## Implementation Overview

This project implements a Graph class representing a weighted, undirected graph using an adjacency list and a separate dictionary for edge weights. The class includes several fundamental graph algorithms.

Key components:
1. Graph class with methods for adding vertices, edges, and retrieving neighbors
2. Implementation of Depth-First Search (DFS)
3. Implementation of Breadth-First Search (BFS)
4. Dijkstra's algorithm implementation using a priority queue (heapq)
5. Performance testing suite for analyzing Dijkstra's algorithm efficiency

## Implemented Algorithms

### 1. Depth-First Search (DFS)

- Purpose: Traverses the graph by exploring as far as possible along each branch before backtracking.
- Implementation: Uses recursive approach with a helper function.
- Use cases: Topological sorting, detecting cycles, path finding in maze-like structures.

### 2. Breadth-First Search (BFS)

- Purpose: Traverses the graph level by level, exploring all neighbors of a vertex before moving to the next level.
- Implementation: Uses an iterative approach with a queue (collections.deque).
- Use cases: Finding shortest path in unweighted graphs, web crawling, social network analysis.

### 3. Dijkstra's Algorithm

- Purpose: Finds the shortest path between a start vertex and all other vertices in a weighted graph.
- Implementation: Uses a priority queue (heapq) to efficiently select the next vertex to process.
- Use cases: GPS navigation, network routing protocols, resource allocation in networks.

## Performance Test Results

Test Environment:
- Date: Aug 23rd 2024
- Python Version: 3.9.6
- Hardware: Apple MacBook Air M1

Results:

| Vertices | Edge Density | Avg. Time (seconds) |
|----------|--------------|---------------------|
| 100      | 0.1          | 0.000148            |
| 100      | 0.5          | 0.000347            |
| 500      | 0.1          | 0.001672            |
| 500      | 0.5          | 0.006673            |
| 1000     | 0.1          | 0.006783            |
| 1000     | 0.5          | 0.029889            |
| 5000     | 0.01         | 0.023794            |
| 5000     | 0.1          | 0.115511            |
| 10000    | 0.001        | 0.020505            |
| 10000    | 0.01         | 0.090739            |

## Analysis

1. Scalability:
   - The algorithm shows good scalability, handling graphs up to 10,000 vertices efficiently.
   - Time complexity appears to be close to the expected O((V + E) log V).

2. Edge Density Impact:
   - Higher edge densities result in longer execution times, as expected.
   - The algorithm remains efficient even with high edge densities (0.5) for medium-sized graphs.

3. Large Sparse Graphs:
   - The implementation performs particularly well on large sparse graphs.
   - A graph with 10,000 vertices and 0.01 edge density is processed in under 0.1 seconds.

4. Small Graph Performance:
   - For small graphs (100 vertices), the algorithm executes in less than a millisecond, suitable for real-time applications.


## Strengths of the Implementation

1. Comprehensive set of fundamental graph algorithms (DFS, BFS, Dijkstra's)
2. Efficient handling of both dense and sparse graphs in Dijkstra's algorithm
3. Good scalability up to 10,000 vertices for Dijkstra's algorithm
4. Fast execution for small to medium-sized graphs across all implemented algorithms
5. Consistent performance across various graph sizes and densities
6. Flexible Graph class design allowing for easy addition of new algorithms

## Potential Improvements

1. Implement iterative DFS for handling very deep graphs without stack overflow
2. Add path reconstruction for BFS to find shortest paths in unweighted graphs
3. Optimize priority queue implementation in Dijkstra's algorithm (e.g., Fibonacci heap) for potentially faster performance on very large graphs
4. Implement bidirectional search for faster path finding in specific scenarios
5. Explore parallelization for processing extremely large graphs
6. Add more advanced graph algorithms like Bellman-Ford (for graphs with negative weights) or Floyd-Warshall (for all-pairs shortest paths)

## Conclusion

The implemented Graph class provides a robust set of fundamental graph algorithms. DFS and BFS offer efficient graph traversal methods, while Dijkstra's algorithm demonstrates strong performance for shortest path problems in weighted graphs. The implementation is suitable for a wide range of applications, from small real-time systems to larger graph processing tasks. The modular design of the Graph class allows for easy extension with additional algorithms in the future.

## Files

1. `graph.py`: Contains the Graph class with DFS, BFS, and Dijkstra's algorithm implementations
2. `graphTest.py`: Contains test cases for various methods in the Graph Class
3. `performanceTest.py`: Performance testing suite for Dijkstra's algorithm
4. `README.md`: This report file
