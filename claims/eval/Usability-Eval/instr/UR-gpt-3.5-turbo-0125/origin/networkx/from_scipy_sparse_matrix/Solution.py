
import networkx as nx
import scipy.sparse as sp

def graph_from_adjacency_list(adjacency_list):
    num_nodes = len(adjacency_list)
    
    edges = []
    for i, neighbors in enumerate(adjacency_list):
        for j in neighbors:
            edges.append((i, j))
    
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    G.add_edges_from(edges)
    
    return G

# Example usage:
# adjacency_list = [[1], [0, 2], [1]]
# G = graph_from_adjacency_list(adjacency_list)
# print(G.nodes)
# print(G.edges)
