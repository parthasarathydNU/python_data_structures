from graph import Graph

def test_graph_initialization():
    print("\nGraph initialization test")
    graph = Graph()
    print("Graph initialization test:", "Pass" if isinstance(graph.graph, dict) and isinstance(graph.weighted_edges, dict) else "Fail")

def test_add_vertex():
    print("\nAdd vertex test")
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    print("Add vertex test:", "Pass" if 1 in graph.graph and 2 in graph.graph else "Fail")
    print("Vertex value test:", "Pass" if graph.graph[1] == [] and graph.graph[2] == [] else "Fail")

def test_add_edge():
    print("\nAdd edge test")
    graph = Graph()
    graph.add_edge(1, 2, 5)
    print("Edge 1-2 test:", "Pass" if 2 in graph.graph[1] and 1 in graph.graph[2] and graph.weighted_edges[1][2] == 5 and graph.weighted_edges[2][1] == 5 else "Fail")
    
    graph.add_edge(1, 3, 7)
    print("Edge 1-3 test:", "Pass" if 3 in graph.graph[1] and 1 in graph.graph[3] and graph.weighted_edges[1][3] == 7 and graph.weighted_edges[3][1] == 7 else "Fail")
    
    # Test adding existing edge with different weight
    graph.add_edge(1, 2, 10)
    print("Update edge weight test:", "Pass" if graph.weighted_edges[1][2] == 10 and graph.weighted_edges[2][1] == 10 else "Fail")
    
    # Test default weight
    graph.add_edge(3, 4)
    print("Default weight test:", "Pass" if graph.weighted_edges[3][4] == 1 and graph.weighted_edges[4][3] == 1 else "Fail")

def test_remove_edge():
    print("\nRemove edge test")
    graph = Graph()
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 7)
    graph.add_edge(2, 3, 6)
    
    graph.remove_edge(1, 2)
    print("Remove edge 1-2 test:", "Pass" if 2 not in graph.graph[1] and 1 not in graph.graph[2] and 2 not in graph.weighted_edges[1] and 1 not in graph.weighted_edges[2] else "Fail")
    
    graph.remove_edge(1, 3)
    print("Remove edge 1-3 test:", "Pass" if 3 not in graph.graph[1] and 1 not in graph.graph[3] and 3 not in graph.weighted_edges[1] and 1 not in graph.weighted_edges[3] else "Fail")
    
    # Test removing non-existent edge
    graph.remove_edge(1, 3)  # This edge was already removed
    print("Remove non-existent edge test:", "Pass" if 3 not in graph.graph[1] and 1 not in graph.graph[3] and (1 not in graph.weighted_edges or 3 not in graph.weighted_edges[1]) else "Fail")
    
    # Test removing edge with non-existent vertex
    graph.remove_edge(1, 4)  # Vertex 4 doesn't exist
    print("Remove edge with non-existent vertex test:", "Pass" if 4 not in graph.graph and 4 not in graph.weighted_edges else "Fail")

def test_get_neighbors():
    print("\nGet neighbors test")
    graph = Graph()
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 7)
    graph.add_edge(2, 3, 6)
    graph.add_edge(3, 4, 8)
    
    neighbors_1 = graph.get_neighbors(1)
    print("Neighbors of 1 test:", "Pass" if set(neighbors_1) == {(2, 5), (3, 7)} else f"Fail. Expected {{(2, 5), (3, 7)}}, got {set(neighbors_1)}")
    
    neighbors_3 = graph.get_neighbors(3)
    print("Neighbors of 3 test:", "Pass" if set(neighbors_3) == {(1, 7), (2, 6), (4, 8)} else f"Fail. Expected {{(1, 7), (2, 6), (4, 8)}}, got {set(neighbors_3)}")
    
    neighbors_5 = graph.get_neighbors(5)
    print("Neighbors of non-existent vertex test:", "Pass" if neighbors_5 == [] else "Fail")

def test_dfs():
    print("\nDFS test")
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    dfs_result = graph.dfs(2)
    print("DFS test:", "Pass" if dfs_result == [2, 0, 1, 3] else f"Fail. Expected [2, 0, 1, 3], got {dfs_result}")

    dfs_result_nonexistent = graph.dfs(4)
    print("DFS non-existent vertex test:", "Pass" if dfs_result_nonexistent == [] else f"Fail. Expected [], got {dfs_result_nonexistent}")

    # Test for disconnected graph
    graph.add_vertex(5)
    graph.add_edge(5, 6)
    dfs_result_disconnected = graph.dfs(0)
    print("DFS disconnected graph test:", "Pass" if set(dfs_result_disconnected) == {0, 1, 2, 3} else f"Fail. Expected {{0, 1, 2, 3}}, got {set(dfs_result_disconnected)}")

def test_bfs():
    print("\nBFS test")
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    bfs_result = graph.bfs(2)
    print("BFS test:", "Pass" if bfs_result == [2, 0, 1, 3] else f"Fail. Expected [2, 0, 1, 3], got {bfs_result}")

    bfs_result_nonexistent = graph.bfs(4)
    print("BFS non-existent vertex test:", "Pass" if bfs_result_nonexistent == [] else f"Fail. Expected [], got {bfs_result_nonexistent}")

    # Test for disconnected graph
    graph.add_vertex(5)
    graph.add_edge(5, 6)
    bfs_result_disconnected = graph.bfs(0)
    print("BFS disconnected graph test:", "Pass" if set(bfs_result_disconnected) == {0, 1, 2, 3} else f"Fail. Expected {0, 1, 2, 3}, got {set(bfs_result_disconnected)}")

def test_dijkstra():
    print("\nDijkstra test")
    graph = Graph()
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 3, 5)
    graph.add_edge(3, 4, 2)

    distance, path = graph.dijkstra(0, 4)
    print("Dijkstra test:", "Pass" if distance == 8 and path == [0, 1, 3, 4] else f"Fail. Expected (8, [0, 1, 3, 4]), got ({distance}, {path})")

    distance, path = graph.dijkstra(0, 5)
    print("Dijkstra no path test:", "Pass" if distance == float('inf') and path == [] else f"Fail. Expected (inf, []), got ({distance}, {path})")

    distance, path = graph.dijkstra(6, 4)
    print("Dijkstra non-existent vertex test:", "Pass" if distance == float('inf') and path == [] else f"Fail. Expected (inf, []), got ({distance}, {path})")

# Run all tests
if __name__ == "__main__":
    test_graph_initialization()
    test_add_vertex()
    test_add_edge()
    test_remove_edge()
    test_get_neighbors()
    test_dfs()
    test_bfs()
    test_dijkstra()
