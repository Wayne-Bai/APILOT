
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from([1, 2, 3])

# Add edges
G.add_edges_from([(1, 2), (2, 3)])

# Calculate HITS scores
hub, authority = nx.hits(G, max_iter=100)

# Print hub matrix
hub_matrix = [hub[node] for node in G.nodes()]
print(hub_matrix)
