
import networkx as nx

# Load your graph from a file or create it manually
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 4), (3, 4)])

# Compute the modularity of the graph using a greedy algorithm
modularity = nx.greedy_modularity(G)

# Print the communities found by the algorithm
print("Communities:", [c for c in modularity])
