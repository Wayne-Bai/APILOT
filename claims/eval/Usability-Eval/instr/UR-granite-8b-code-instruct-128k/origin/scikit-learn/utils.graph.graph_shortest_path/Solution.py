from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

def shortest_path_graph_search(graph, start, end, threshold=1e-6):
    if not isinstance(graph, np.ndarray):
        graph = np.array(graph)
    if graph.ndim == 1:
        graph = graph.reshape(1, -1)
    num_nodes = graph.shape[1]
    distances = euclidean_distances(graph)
    if not np.all(np.linalg.eigvals(distances) > 0):
        raise ValueError("Graph is not positive definite.")
    visited = np.zeros(num_nodes, dtype=bool)
    queue = [start]
    visited[start] = True
    paths = {start: [start]}
    while queue:
        node = queue.pop(0)
        for neighbor in range(num_nodes):
            if visited[neighbor]:
                continue
            if distances[node, neighbor] < threshold:
                new_path = paths[node].copy()
                new_path.append(neighbor)
                paths[neighbor] = new_path
                queue.append(neighbor)
                if neighbor == end:
                    return paths[neighbor]
    return None
