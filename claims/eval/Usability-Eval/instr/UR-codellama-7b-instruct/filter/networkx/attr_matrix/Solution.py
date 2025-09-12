
import networkx as nx

def get_attribute_matrix(G):
    # construct the adjacency matrix if not provided
    if type(G) == nx.classes.graph.Graph:
        G = nx.adjacency_matrix(G, dtype=float)
    else:
        raise ValueError("Invalid graph type")

    # get the number of nodes and edges in the graph
    num_nodes = G.shape[0]
    num_edges = G.count_nonzero()

    # initialize an empty attribute matrix with the correct dimensions
    attr_matrix = np.empty((num_nodes, num_edges), dtype=int)

    # iterate over each edge and set its corresponding value in the attribute matrix
    for i, j in zip(G.row, G.col):
        attr_matrix[i][j] = 1

    return attr_matrix
