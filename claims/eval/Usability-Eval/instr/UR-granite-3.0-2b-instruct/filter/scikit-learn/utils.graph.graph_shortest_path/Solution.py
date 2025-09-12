from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

def shortest_path(graph, start, end):
    # Calculate the distance matrix using Euclidean distances
    distance_matrix = euclidean_distances(graph, graph)

    # Find the shortest path using Dijkstra's algorithm
    path = np.zeros(len(graph), dtype=int)
    path[start] = 0
    unvisited = np.ones(len(graph), dtype=bool)
    unvisited[start] = False

    while np.any(unvisited):
        current = np.argmin(distance_matrix[np.where(unvisited)[0], :])
        unvisited[current] = False

        for neighbor in range(len(graph)):
            if graph[current, neighbor] != 0 and unvisited[neighbor]:
                distance = distance_matrix[current, neighbor] + path[neighbor]
                if distance < distance_matrix[current, neighbor]:
                    distance_matrix[current, neighbor] = distance
                    distance_matrix[neighbor, current] = distance
                    path[neighbor] = distance_matrix[current, neighbor]

    return path

# Example usage:
# Create a positive directed graph
graph = np.array([[0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1],
                  [0, 0, 0, 0]])

# Find the shortest path from node 0 to node 3
path = shortest_path(graph, 0, 3)
print(path)
