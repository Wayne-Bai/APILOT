import networkx as nx
import random

# Create an empty directed graph
G = nx.DiGraph()

# Add nodes in a consistent order
num_nodes = 10
for i in range(num_nodes):
    G.add_node(i)

# Add edges
num_edges = 15
node_list = list(G.nodes())
for i in range(num_edges):
    u = random.choice(node_list)
    v = random.choice(node_list)
    if u!= v:
        G.add_edge(u, v)

# Print edges in a consistent order
print('Edges in a consistent order:')
print(G.edges())

# Create an ordered directed graph
OG = nx.OrderedDiGraph()

# Add nodes in a consistent order
for i in range(num_nodes):
    OG.add_node(i)

# Add edges
for i in range(num_edges):
    u = random.choice(node_list)
    v = random.choice(node_list)
    if u!= v:
        OG.add_edge(u, v)

# Print edges in a consistent order
print('\nEdges in a consistent order (OrderedDiGraph):')
print(OG.edges())
