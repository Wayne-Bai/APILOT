import networkx as nx

# Creating a graph
G = nx.Graph()

# Adding edges to the graph, basically connecting nodes
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('D', 'E')

# Consuming the iterator entirely (traversing the graph)
print("Node List: ", list(G.nodes()))

