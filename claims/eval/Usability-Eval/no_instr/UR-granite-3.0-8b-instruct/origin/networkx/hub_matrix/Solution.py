import networkx as nx

def hub_matrix(G):
    # Calculate the hub scores for each node
    hub_scores = nx.hits_hubs(G)

    # Create a dictionary with the hub scores
    hub_dict = dict(zip(G.nodes(), hub_scores[0]))

    # Create a matrix with the hub scores
    hub_matrix = nx.to_numpy_array(hub_dict)

    return hub_matrix
