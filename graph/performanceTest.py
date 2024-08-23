import time
import random
from graph import Graph

def generate_random_graph(num_vertices, edge_density):
    graph = Graph()
    for i in range(num_vertices):
        graph.add_vertex(i)
    
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if random.random() < edge_density:
                weight = random.randint(1, 100)
                graph.add_edge(i, j, weight)
    
    return graph

def performance_test_dijkstra(num_vertices, edge_density, num_trials):
    total_time = 0
    graph = generate_random_graph(num_vertices, edge_density)
    
    for _ in range(num_trials):
        start = random.randint(0, num_vertices - 1)
        end = random.randint(0, num_vertices - 1)
        
        start_time = time.time()
        graph.dijkstra(start, end)
        end_time = time.time()
        
        total_time += (end_time - start_time)
    
    avg_time = total_time / num_trials
    print(f"Average time for {num_vertices} vertices, {edge_density} edge density: {avg_time:.6f} seconds")

def run_performance_tests():
    print("Running Dijkstra's Algorithm Performance Tests")
    print("----------------------------------------------")

    test_cases = [
        (100, 0.1, 100),
        (100, 0.5, 100),
        (500, 0.1, 50),
        (500, 0.5, 50),
        (1000, 0.1, 20),
        (1000, 0.5, 20),
        (5000, 0.01, 10),
        (5000, 0.1, 10),
        (10000, 0.001, 5),
        (10000, 0.01, 5)
    ]

    for vertices, density, trials in test_cases:
        performance_test_dijkstra(vertices, density, trials)

if __name__ == "__main__":
    run_performance_tests()
