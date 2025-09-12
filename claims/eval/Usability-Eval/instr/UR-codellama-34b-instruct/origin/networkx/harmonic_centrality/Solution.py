
import networkx as nx

# Create a graph object
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D')])

# Compute harmonic centrality for nodes
centralities = nx.harmonic_centrality(G)

print("Harmonic centrality:")
for node, centrality in centralities.items():
    print(f"{node}: {centrality}")
