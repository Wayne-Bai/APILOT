import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes to the graph
# Please replace the nodes with your own nodes
nodes = ['A', 'B', 'C', 'D']
G.add_nodes_from(nodes)

# Add edges to the graph
# Please replace the edges with your own edges
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]
G.add_edges_from(edges)

# Calculate communicability between all pairs of nodes
communicability = nx.communicability_exp(G)

# Print the communicability
for node1, comm_dict in communicability.items():
    for node2, comm_val in comm_dict.items():
        print(f'Communicability between {node1} and {node2} is: {comm_val}')
