
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add some nodes and edges to the graph
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C')])

# Get the triadic census of the graph
triads = nx.triadic_census(G, nodelist=['A', 'B'])
print(triads)
