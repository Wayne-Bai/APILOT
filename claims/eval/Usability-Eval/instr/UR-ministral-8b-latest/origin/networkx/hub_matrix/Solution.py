import networkx as nx

def hits_hub_matrix(G):
    hub_node = nx.hits_hub(G)[1]
    authority_node = nx.hits_authority(G)[1]
    hub_matrix = dict(zip(hub_node, authority_node.values()))

    return hub_matrix

# Example usage:
G = nx.Graph()
G.add_edges_from([
    (0, 1), (0, 2), (1, 3), (1, 4),
    (1, 5), (1, 6), (2, 3), (2, 4),
    (2, 5), (3, 5), (3, 6)
])

hits_matrix = hits_hub_matrix(G)
print(hits_matrix)
