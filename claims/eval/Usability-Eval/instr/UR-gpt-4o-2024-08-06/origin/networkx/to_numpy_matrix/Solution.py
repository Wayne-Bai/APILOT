import networkx as nx
import numpy as np

def graph_to_adjacency_matrix(graph):
    # Convert the graph to an adjacency matrix and return it as a numpy array
    adjacency_dict = nx.to_dict_of_dicts(graph)
    nodes = list(graph.nodes())
    adj_matrix = np.zeros((len(nodes), len(nodes)), dtype=int)
    
    for i, node_i in enumerate(nodes):
        for j, node_j in enumerate(nodes):
            if node_j in adjacency_dict[node_i]:
                adj_matrix[i, j] = 1
    
    return adj_matrix

# Example Usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (4, 1), (3, 4)])
adj_matrix = graph_to_adjacency_matrix(G)
print(adj_matrix)
