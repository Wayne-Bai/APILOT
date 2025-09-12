import networkx as nx

def create_graph_from_sparse_matrix(sparse_matrix):
    # Convert the sparse matrix to a list of edges
    edges = list(zip(sparse_matrix.row, sparse_matrix.col))

    # Create a directed graph from the list of edges
    G = nx.DiGraph()
    G.add_edges_from(edges)

    return G
