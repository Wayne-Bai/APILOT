import networkx as nx

# Create a sample graph
G = nx.cyclic_graph(5)

# Example of an iterator in NetworkX - iterate through nodes
node_iterator = iter(G.nodes())

# Consume the iterator entirely
nodes = list(node_iterator)
print("Nodes in the graph:", nodes)
