import networkx as nx

def get_google_matrix(G):
    """Returns the Google matrix of the graph G."""
    # Get the number of nodes in the graph
    num_nodes = len(G.nodes)

    # Initialize an empty matrix with dimensions (num_nodes, num_nodes)
    google_matrix = np.zeros((num_nodes, num_nodes))

    # Iterate over each node in the graph
    for node in G.nodes:
        # Get the shortest path lengths from the current node to all other nodes in the graph
        dist = nx.shortest_path(G, source=node)

        # Add the shortest path length values to the corresponding entries in the Google matrix
        for i in range(num_nodes):
            google_matrix[i][node] += dist[i]

    return google_matrix
