import networkx as nx

# Create a new directed graph
G = nx.DiGraph()

# Add nodes and unique labels
for i in range(10):
    G.add_node(i, label="Node {}".format(i))

# Trace the operation
print(list(G.nodes(data='label')))
