import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add some edges to the graph
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')
G.add_edge('A', 'D')
G.add_edge('D', 'E')

# Return the adjacency matrix of G
def get_adjacency_matrix(G):
    return nx.to_numpy_array(G)

adjacency_matrix = get_adjacency_matrix(G)
print(adjacency_matrix)
