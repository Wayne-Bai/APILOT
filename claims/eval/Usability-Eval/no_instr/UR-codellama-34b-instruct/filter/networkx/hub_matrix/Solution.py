
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node('A')
G.add_node('B')
G.add_edge('A', 'B')

# Compute the HITS hub matrix using the NetworkX library
H = nx.hits(G, alpha=0.85)

print(H)
