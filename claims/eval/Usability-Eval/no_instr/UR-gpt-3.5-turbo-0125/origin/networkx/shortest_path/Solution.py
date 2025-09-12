
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges with weights
G.add_edge(1, 2, weight=1)
G.add_edge(2, 3, weight=2)
G.add_edge(1, 3, weight=3)
G.add_edge(3, 4, weight=1)
G.add_edge(4, 5, weight=2)
G.add_edge(1, 5, weight=4)

# Compute the shortest path
shortest_path = nx.shortest_path(G, source=1, target=5, weight='weight')
print("Shortest path from Node 1 to Node 5:", shortest_path)
