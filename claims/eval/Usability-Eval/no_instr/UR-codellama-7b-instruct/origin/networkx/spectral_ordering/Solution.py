
from networkx import Graph
import numpy as np

def spectral_ordering(G):
    """
    Compute the spectral ordering of a graph using NetworkX.

    Args:
        G (networkx.Graph): The graph to be ordered.

    Returns:
        list[int]: A list of integers representing the nodes in the graph, with
            nodes in the same weakly connected component appearing contiguous and
            ordered by their corresponding elements in the Fiedler vector of the
            component.
    """
    # Compute the Fiedler vector of each weakly connected component
    wccs = [wcc for wcc in nx.weakly_connected_components(G)]
    fiedler_vectors = [np.asarray(nx.fiedler_vector(G, wcc)) for wcc in wccs]

    # Compute the ordering of the nodes within each weakly connected component
    node_orderings = []
    for i, wcc in enumerate(wccs):
        fiedler_vector = fiedler_vectors[i]
        node_ordering = np.argsort(-fiedler_vector)  # sort by descending order of Fiedler vector elements
        node_ordering = [node for node in wcc if node in G]  # filter out nodes that are not in the graph G
        node_orderings.append(node_ordering)

    # Combine the node orderings from each weakly connected component into a single ordering of all nodes
    global_node_order = []
    for i, wcc in enumerate(wccs):
        node_ordering = node_orderings[i]
        global_node_order.extend(node_ordering)

    return global_node_order
