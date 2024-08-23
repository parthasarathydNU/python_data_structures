import unittest
from graph import Graph

class TestTopologicalSort(unittest.TestCase):

    def test_simple_dag(self):
        graph = Graph(directed=True)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 3)

        result = graph.topological_sort()
        self.assertTrue(self.is_valid_topological_order(graph, result))
        self.assertEqual(set(result), {0, 1, 2, 3})

    def test_larger_dag(self):
        graph = Graph(directed=True)
        graph.add_edge(5, 2)
        graph.add_edge(5, 0)
        graph.add_edge(4, 0)
        graph.add_edge(4, 1)
        graph.add_edge(2, 3)
        graph.add_edge(3, 1)

        result = graph.topological_sort()
        self.assertTrue(self.is_valid_topological_order(graph, result))
        self.assertEqual(set(result), {0, 1, 2, 3, 4, 5})

    def test_dag_with_multiple_valid_orderings(self):
        graph = Graph(directed=True)
        graph.add_edge(3, 1)
        graph.add_edge(3, 2)
        graph.add_edge(1, 0)
        graph.add_edge(2, 0)

        result = graph.topological_sort()
        self.assertTrue(self.is_valid_topological_order(graph, result))
        self.assertEqual(set(result), {0, 1, 2, 3})

    def test_single_vertex(self):
        graph = Graph(directed=True)
        graph.add_vertex(0)

        result = graph.topological_sort()
        self.assertEqual(result, [0])

    def test_empty_graph(self):
        graph = Graph(directed=True)

        result = graph.topological_sort()
        self.assertEqual(result, [])

    def test_graph_with_cycle(self):
        graph = Graph(directed=True)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)

        with self.assertRaises(Exception):
            graph.topological_sort()

    def test_disconnected_dag(self):
        graph = Graph(directed=True)
        graph.add_edge(0, 1)
        graph.add_edge(2, 3)
        graph.add_vertex(4)

        result = graph.topological_sort()
        self.assertTrue(self.is_valid_topological_order(graph, result))
        self.assertEqual(set(result), {0, 1, 2, 3, 4})

    def test_complex_dag(self):
        graph = Graph(directed=True)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 4)
        graph.add_edge(3, 5)
        graph.add_edge(4, 5)

        result = graph.topological_sort()
        self.assertTrue(self.is_valid_topological_order(graph, result))
        self.assertEqual(set(result), {0, 1, 2, 3, 4, 5})

    def is_valid_topological_order(self, graph, order):
        visited = set()
        for v in order:
            for neighbor, _ in graph.get_neighbors(v):
                if neighbor in visited:
                    return False
            visited.add(v)
        return len(visited) == len(graph.graph)

if __name__ == '__main__':
    unittest.main()
