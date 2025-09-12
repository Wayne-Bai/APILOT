import networkx as nx

# Define the small graph described by graph_description
graph_description = {
    'nodes': {
        'A': {},
        'B': {},
        'C': {}
    },
    'edges': [
        ('A', 'B'),
        ('B', 'C')
    ]
}

# Create a new graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(graph_description['nodes'])

# Add edges to the graph
G.add_edges_from(graph_description['edges'])

# Return the small graph described by graph_description
return G