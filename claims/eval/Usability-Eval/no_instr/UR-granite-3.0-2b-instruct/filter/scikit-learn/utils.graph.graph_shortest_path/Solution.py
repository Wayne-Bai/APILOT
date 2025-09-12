from sklearn.metrics.pairwise import pairwise_distances

def shortest_path(graph, start, end):
    distances = pairwise_distances(graph, start, end)
    return distances

# Example usage:
# Create a graph (2D array)
graph = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]

# Perform shortest-path graph search
start = 0
end = 2
distances = shortest_path(graph, start, end)

print("Shortest path distances:", distances)
