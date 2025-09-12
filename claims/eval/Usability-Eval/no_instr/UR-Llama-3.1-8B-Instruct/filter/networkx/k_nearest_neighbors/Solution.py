import networkx as nx
import matplotlib.pyplot as plt

def compute_average_degree_connectivity(G, min_degree=None, max_degree=None):
    """
    Compute the average degree connectivity of graph.

    Parameters:
    G (networkx.Graph): The input graph
    min_degree (int, optional): Minimum degree of nodes to consider. Defaults to None.
    max_degree (int, optional): Maximum degree of nodes to consider. Defaults to None.

    Returns:
    dict: Average degree connectivity of nodes with degree k
    """
    avg_degree_connectivity = {}

    # Get all degrees in the graph
    degrees = sorted(list(nx.degree(G)))

    for k in range(min_degree, max_degree + 1) if min_degree is not None and max_degree is not None else (min(degrees) if min_degree is None else [min_degree, max(degrees)]):
        # Get nodes with degree k
        nodes_with_degree_k = [node for node, degree in degrees if degree == k]

        sum_nn_degree = 0
        # For each node with degree k, count the sum of nearest neighbor degrees
        for node in nodes_with_degree_k:
            node_neighs = G.neighbors(node)
            sum_nn_degree += sum(nx.degree(G, nei) for nei in node_neighs)

        # average over the number of neighbors nodes with degree k have
        avg_degree_connectivity[k] = sum_nn_degree / (len(nodes_with_degree_k) * len(G.neighbors(nodes_with_degree_k[0])))

    return avg_degree_connectivity

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# Print the average degree connectivity of the sample graph
print(compute_average_degree_connectivity(G))

# Display the graph with networkx
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
