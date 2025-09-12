import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(['A', 'B', 'C'])
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'A')])

# Set the node attribute 'label' to the node name
for n in G.nodes:
    G.nodes[n]['label'] = n

# Set the edge attribute 'weight' to 1 for all edges
for u, v in G.edges:
    G.edges[u, v]['weight'] = 1

# Export the graph to JIT JSON format
nx.write_jit(G, 'graph.json')
