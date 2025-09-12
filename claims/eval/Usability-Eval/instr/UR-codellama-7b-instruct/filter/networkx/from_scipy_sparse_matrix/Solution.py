import networkx as nx
from scipy import sparse

def get_graph_from_scipy_sparse_matrix(adjacency_list):
    """
    Return a graph from a SciPy sparse matrix adjacency list.
    :param adjacency_list: The adjacency list of the graph in SciPy sparse format.
    :return: A NetworkX graph object.
    """
    num_nodes = adjacency_list.shape[0]
    G = nx.DiGraph()  # create an empty directed graph
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if adjacency_list[i][j] != 0:  # check if there is an edge between nodes i and j
                G.add_edge(i, j)
    return G
