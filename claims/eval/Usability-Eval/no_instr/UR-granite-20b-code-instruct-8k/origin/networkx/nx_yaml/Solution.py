import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node(1, name='Node 1')
G.add_node(2, name='Node 2')
G.add_edge(1, 2, weight=0.5)

# Write the graph to a YAML file
nx.write_yaml(G, 'graph.yaml')

# Read the graph from the YAML file
H = nx.read_yaml('graph.yaml')
