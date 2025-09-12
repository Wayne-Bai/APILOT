import networkx as nx

# Create an empty graph
G = nx.Graph()

# Create an iterator
iterator = iter([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')])

# Consume the iterator entirely
while True:
    try:
        node1, node2 = next(iterator)
        G.add_edge(node1, node2)
    except StopIteration:
        break

# Print the graph
print(G.nodes())
print(G.edges())
