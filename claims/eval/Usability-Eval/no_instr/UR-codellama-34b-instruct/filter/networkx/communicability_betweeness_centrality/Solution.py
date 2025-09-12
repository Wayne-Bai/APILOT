import networkx as nx

# Define the graph
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C'])
G.add_edges_from([('A', 'B'), ('B', 'C')])

# Calculate subgraph communicability for all pairs of nodes
subgraphs = []
for u in G.nodes():
    for v in G.nodes():
        if u != v and nx.is_connected(G, u, v):
            subgraphs.append((u, v))

# Print the results
print('Subgraph communicability for all pairs of nodes:')
for u, v in subgraphs:
    print(f'{u} and {v}: {nx.subgraph_connectivity(G, u, v)}')
