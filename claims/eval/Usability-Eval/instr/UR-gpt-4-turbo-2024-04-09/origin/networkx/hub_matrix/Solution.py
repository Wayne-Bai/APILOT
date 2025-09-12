import networkx as nx

def hits_hub_matrix(G):
    # Compute the HITS algorithm
    h, a = nx.hits(G)
    # Create a matrix of hub values
    hub_matrix = nx.to_numpy_array(G, nodelist=sorted(G.nodes()), weight=None)
    for i, node in enumerate(sorted(G.nodes())):
        hub_matrix[i] = h[node]
    return hub_matrix

# Example usage:
# Create a directed graph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 2)])

# Calculate the HITS Hub matrix
hub_matrix = hits_hub_matrix(G)
print(hub_matrix)
