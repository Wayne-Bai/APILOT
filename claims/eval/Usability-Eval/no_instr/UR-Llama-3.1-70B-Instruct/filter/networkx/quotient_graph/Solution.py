import networkx as nx
from collections import defaultdict

def quotient_graph(G, partition):
    """
    Returns the quotient graph of G under the specified equivalence relation on nodes.

    Parameters:
    G (networkx Graph): The original graph.
    partition (dict): A dictionary assigning each node to an equivalence class.

    Returns:
    quotient (networkx Graph: The quotient graph of G.
    """
    # Create a new graph to store the quotient graph
    H = nx.Graph()
    
    # Add nodes to the quotient graph
    for node_set in set(partition.values()):
        H.add_node(node_set)

    # Add edges to the quotient graph if there is at least one edge in the original graph
    for u in G.nodes():
        for v in G.nodes():
            if u!= v and partition[u]!= partition[v] and G.has_edge(u, v):
                H.add_edge(partition[u], partition[v])

    return H


# Usage example:
if __name__ == "__main__":
    # Create a graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (4, 6)])

    # Define a node equivalence relation
    partition = {1: 'A', 2: 'A', 3: 'A', 4: 'B', 5: 'B', 6: 'B'}

    # Calculate the quotient graph
    H = quotient_graph(G, partition)

    # Print the quotient graph
    print(nx.nodes(H))
    print(nx.edges(H))
