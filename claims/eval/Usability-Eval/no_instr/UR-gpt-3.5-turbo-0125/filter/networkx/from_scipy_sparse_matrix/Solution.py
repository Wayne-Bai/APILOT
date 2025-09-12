
import networkx as nx
import scipy.sparse as sp

def graph_from_adjacency_list(adjacency_list):
    rows, cols = adjacency_list.nonzero()
    graph = nx.Graph()
    
    for i, j in zip(rows, cols):
        graph.add_edge(i, j)
    
    return graph

# Sample adjacency matrix (sparse) list for testing
adjacency_list = sp.lil_matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

# Create graph from adjacency list
graph = graph_from_adjacency_list(adjacency_list)
print(nx.info(graph))
