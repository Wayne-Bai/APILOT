import networkx as nx

def attribute_mixing_matrix(G, attribute):
    return nx.attribute_mixing_matrix(G, attribute)

# Example usage
G = nx.Graph()
G.add_nodes_from([
    (1, {'color': 'red'}),
    (2, {'color': 'blue'}),
    (3, {'color': 'red'}),
    (4, {'color': 'blue'})
])
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

matrix = attribute_mixing_matrix(G, 'color')
print(matrix)
