import networkx as nx

def calculate_hits_authority(graph):
    hits = nx.hits(graph)
    return hits[0]  # return authority matrix

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

# Calculate HITS authority
authority_matrix = calculate_hims_authority(G)
print(f"HITS Authority Matrix: {authority_matrix}")
