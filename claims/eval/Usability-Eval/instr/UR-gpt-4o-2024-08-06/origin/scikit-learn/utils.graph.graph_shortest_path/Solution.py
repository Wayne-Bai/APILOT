import numpy as np
from heapq import heappop, heappush

def dijkstra_shortest_path(graph, source, target):
    # Number of nodes
    num_nodes = len(graph)
    
    # Initialize distances of all nodes as infinite.
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0
    
    # Use a priority queue to store (distance, node) pairs
    priority_queue = [(0, source)]
    
    # Dictionary to store the path leading to each node
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        # Extract the node with the smallest distance
        current_distance, current_node = heappop(priority_queue)
        
        # If we reached the target node, we can break early
        if current_node == target:
            break
        
        # If a node is popped from the queue with a larger distance than
        # the current known shortest distance, we skip processing it
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heappush(priority_queue, (distance, neighbor))
                
    # Reconstruct the path and return it
    path, current_node = [], target
    while previous_nodes[current_node] is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    if path:
        path.insert(0, current_node)
    return path, distances[target]

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

shortest_path, path_distance = dijkstra_shortest_path(graph, 'A', 'D')
print(f"Shortest path: {shortest_path} with total distance: {path_distance}")
