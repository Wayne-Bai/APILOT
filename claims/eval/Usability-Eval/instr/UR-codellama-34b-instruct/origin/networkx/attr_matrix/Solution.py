import networkx as nx

# Define a graph with attributes
G = nx.Graph()
G.add_nodes_from([(1, {"attr1": "value1", "attr2": "value2"}), (2, {"attr3": "value3", "attr4": "value4"})])
G.add_edges_from([(1, 2, {"weight": 0.5}), (2, 3, {"weight": 0.7})])

# Get the attribute matrix using NetworkX
A = nx.get_attribute_matrix(G)
print(A)
