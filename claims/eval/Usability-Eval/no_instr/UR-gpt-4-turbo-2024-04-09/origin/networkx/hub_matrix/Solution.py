import networkx as nx

def hits_hub_matrix(G):
    h, a = nx.hits(G)
    return nx.to_numpy_matrix(G, nodelist=sorted(G.nodes()), weight=None), h

# Example usage
# Create a directed graph
G = nx.DiGraph()
# Add some edges
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')
G.add_edge('B', 'D')

# Get the HITS hub matrix
hub_matrix, hubs = hits_hub_matrix(G)
print("HITS Hub Matrix:")
print(hub_matrix)
print("Hub scores:", hubs)
