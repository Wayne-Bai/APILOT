import networkx as nx
from scipy.sparse import csr_matrix

def adj_matrix_to_graph(adj_matrix):
    # Create an empty graph
    G = nx.Graph()

    # Get the number of nodes
    num_nodes = adj_matrix.shape[0]

    # Convert the adjacency matrix to an adjacency list
    adj_list = adj_matrix.todense().tolist()
    for i in range(num_nodes):
        for j in range(num_nodes):
            if adj_list[i][j] == 1:  # Assuming 1 represents an edge
                G.add_edge(i, j)

    return G

# Example usage
adj_matrix = csr_matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
adj_graph = adj_matrix_to_graph(adj_matrix)

# Print the graph
print(nx.to_numpy_array(adj_graph))
