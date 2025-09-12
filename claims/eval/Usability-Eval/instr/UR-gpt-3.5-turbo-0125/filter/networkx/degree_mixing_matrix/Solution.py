
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes with attributes
G.add_node(1, attribute='A')
G.add_node(2, attribute='B')
G.add_node(3, attribute='C')

# Add edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)

# Initialize mixing matrix
mixing_matrix = dict()

# Calculate mixing matrix for attribute
for node in G.nodes:
    node_attr = G.nodes[node]['attribute']
    neighbors = list(G.successors(node)) + list(G.predecessors(node))
    
    mixing_matrix[node_attr] = {attr: neighbors.count(attr) for attr in set(neighbors)}

print(mixing_matrix)
