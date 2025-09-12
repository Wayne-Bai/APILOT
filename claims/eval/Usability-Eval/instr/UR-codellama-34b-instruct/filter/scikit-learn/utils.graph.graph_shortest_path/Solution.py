from sklearn.graph import ShortestPathGraph

# Define the graph
G = np.array([[0, 1], [1, 2], [2, 3], [3, 4]])

# Create a shortest-path graph object
spg = ShortestPathGraph(G)

# Get the shortest path between two nodes
print("Shortest path between node 0 and 4:", spg.get_shortest_path(0, 4))
