from typing import List, Tuple
from collections import deque
import heapq

class Graph:

    def __init__(self) -> None:
        self.graph = {}
        self.weighted_edges = {}

    def add_vertex(self, vertex: int) -> None:
        if vertex in self.graph:
            pass
        else:
            self.graph[vertex] = []

    def _add_weighted_edge(self, a: int, b: int, weight: int):
        if a not in self.weighted_edges:
            self.weighted_edges[a] = {}
        
        if b not in self.weighted_edges[a]:
            self.weighted_edges[a][b] = 1

        self.weighted_edges[a][b] = weight

    def _rem_weighted_edge(self, a: int, b: int):
        
        if a not in self.weighted_edges or b not in self.weighted_edges[a]:
            pass
        else :
            del self.weighted_edges[a][b]

    def add_edge(self, a: int, b: int, weight: int = 1) -> None:
        if a not in self.graph:
            self.add_vertex(a)
        if b not in self.graph:
            self.add_vertex(b)

        # avoid adding duplicates
        if b not in self.graph[a]:
            self.graph[a].append(b)

        if a not in self.graph[b]:   
            self.graph[b].append(a)

        # Weights can be updated even if the edges are present    
        self._add_weighted_edge(a, b, weight)
        self._add_weighted_edge(b, a, weight)

    def remove_edge(self, a: int, b: int) -> None:

        if a not in self.graph or b not in self.graph:
            return

        if b in self.graph[a]:
            index = self.graph[a].index(b)
            self.graph[a].pop(index)

            # Remove edge a - b
            self._rem_weighted_edge(a, b)

        if a in self.graph[b]:
            index = self.graph[b].index(a)
            self.graph[b].pop(index)
            
            self._rem_weighted_edge(b, a)

    def get_neighbors(self, a: int) -> List[Tuple[int, int]]:
        """
        Returns a list of tuple(neighbourNode, weight from a to neighbour)
        """
        neighbours = []

        if a not in self.graph:
            return neighbours
        else: 
            neighbours = self.graph[a]

        return [(neighbour, self.weighted_edges[a][neighbour]) for neighbour in neighbours]


    def dfs(self, a: int) -> List[int]:

        if a not in self.graph:
            return []

        visited = []
        self._dfs_helper(a, visited)
        
        return visited

    def _dfs_helper(self, vertex: int, visited: List[int]):

        # We get into this function call only when this node has not been visited
        # The check for visited needs to happen before calling this function        
        visited.append(vertex)

        neighbours = [ neighbour for (neighbour, edge)  in self.get_neighbors(vertex)]

        for neighbor in neighbours:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)

    def bfs(self, a: int) -> List[int]:
        if a not in self.graph:
            return []

        visited = []

        queue = deque()

        queue.appendleft(a)

        while len(queue) > 0:
            node = queue.pop()

            if node in visited:
                continue

            visited.append(node)

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    queue.appendleft(neighbour)

        return visited

    def dijkstra(self, start:int, end: int)-> Tuple[int, List[int]]:
        """
        https://www.youtube.com/watch?v=EFg3u_E6eHU
        Finds the shortest path between a starting node 
        and all other nodes in a weighted graph

        Particularly useful for graphs for non-negative edge weights

        Greedy Approach: Make locally optimal choice at each step hoping to find global optimum
        Distance Array: Maintain array of shortest distance from start node to each node
        Visited Set: Keep track of nodes whose shortest distance from start node has been found
        Priority Queue: Use a min pq to effeciently select the unvisited node with smallest tentative distance

        Total time complexity is O( (V + E)log(v) )
        """

        if start not in self.graph or end not in self.graph:
            return float('inf'), []     

        # initializing the distances to reach a node from the start node
        distances = {node: float('inf') for node in self.graph}   # O(v)
        distances[start] = 0

        # List to keep track of provious node in optimal path to a given node
        # from the start node 
        previous_node = {node: None for node in self.graph} # O(v)

        # Priority queue to store the vertices to visit next
        pq = [(0, start)] 

        while pq: # O(V)

            # get the vertex with the smallest distance
            current_distance, current_vertex = heapq.heappop(pq) # O(logV)

            # If we have reached the end vertex, we are done
            if current_vertex == end:
                path = []
                while current_vertex:
                    path.append(current_vertex)
                    current_vertex = previous_node[current_vertex]
                
                path.append(start)
                return current_distance, path[::-1] # probably this reverses the array
            
            # If we have found a longer path, then we skip
            if current_distance > distances[current_vertex]:
                continue

            # We have found a node, for which we have arrived from a different
            # Path where the current_distance is smaller than the 
            # previously known distance to reach that vertex

            for neighbour, weight in self.get_neighbors(current_vertex):
                distance = current_distance + weight

                # Only if the new distance to this node is shorter than the already
                # Found distance, we update it
                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    previous_node[neighbour] = current_vertex
                    heapq.heappush(pq, (distance, neighbour))


        return float('inf'), []
   
