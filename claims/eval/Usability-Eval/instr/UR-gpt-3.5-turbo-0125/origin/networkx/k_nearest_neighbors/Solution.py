
import networkx as nx

def average_degree_connectivity(graph):
    avg_degree_connectivity = nx.average_degree_connectivity(graph)
    return avg_degree_connectivity

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3)])
result = average_degree_connectivity(G)
print(result)
