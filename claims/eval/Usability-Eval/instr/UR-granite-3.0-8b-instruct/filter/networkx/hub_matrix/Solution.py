import networkx as nx

def hits_hub_matrix(graph):
    """
    Calculate the HITS hub matrix for a given graph.

    :param graph: networkx graph
    :return: hub matrix
    """
    hubs, authorities = nx.hits(graph)
    return hubs

# Example usage:
G = nx.path_graph(10)  # Create a path graph with 10 nodes
hub_matrix = hits_hub_matrix(G)
print(hub_matrix)
