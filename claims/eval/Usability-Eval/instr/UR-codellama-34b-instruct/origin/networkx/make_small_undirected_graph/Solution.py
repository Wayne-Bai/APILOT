import networkx as nx

# Create a graph object
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(['A', 'B', 'C'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C')])

# Get a dictionary of node degrees (in-degree and out-degree)
node_degrees = G.degree()

# Print the degree of each node
for node, degree in node_degrees:
    print(f'{node}: {degree}')
