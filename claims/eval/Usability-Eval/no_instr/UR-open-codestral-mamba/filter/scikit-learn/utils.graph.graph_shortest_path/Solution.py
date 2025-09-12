from sklearn.metrics.pairwise import haversine_distances
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Function for calculating dijkstra's algorithm
def dijkstra(graph, start, end):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}

    for node in unvisited_nodes:
        shortest_path[node] = float('inf')
    shortest_path[start] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors = graph.get_neighbors(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.get_edge_weight(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value

        unvisited_nodes.remove(current_min_node)

    return shortest_path[end]

# Creating graph
class Graph:
    def __init__(self, nodes, is_directed=True):
        self.graph = {}
        self.is_directed = is_directed
        self.nodes = nodes

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {node2: weight}
        else:
            self.graph[node1][node2] = weight

        if not self.is_directed:
            if node2 not in self.graph:
                self.graph[node2] = {node1: weight}
            else:
                self.graph[node2][node1] = weight

    def get_neighbors(self, node):
        return list(self.graph[node].keys())

    def get_edge_weight(self, node1, node2):
        return self.graph[node1][node2]

    def get_nodes(self):
        return self.nodes

# Creating graph
nodes = ['A', 'B', 'C', 'D', 'E']
graph = Graph(nodes)

# Adding edges with weight
graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 1)
graph.add_edge('B', 'D', 2)
graph.add_edge('C', 'D', 8)
graph.add_edge('D', 'E', 3)

# Shortest path from 'A' to 'E'
print(dijkstra(graph, 'A', 'E'))
