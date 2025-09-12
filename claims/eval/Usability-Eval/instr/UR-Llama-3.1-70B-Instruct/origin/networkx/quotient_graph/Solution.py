import networkx as nx
from collections import defaultdict

def quotient_graph(G, partition):
    """
    Returns the quotient graph of G under the specified equivalence relation on nodes.
    
    The nodes of the quotient graph are the set of unique labels in the partition dictionary. 
    The edges in the quotient graph are between two unique labels if there is an edge in the original graph 
    between any two nodes with these labels.

    Parameters
    ----------
    G : NetworkX graph
    partition : dictionary mapping nodes of G to labels

    Returns
    -------
    NetworkX graph
    """
    # Create an empty graph
    Q = nx.Graph()
    
    # Add nodes for each unique label in the partition
    for label in set(partition.values()):
        Q.add_node(label)

    # Add edges in the quotient graph
    for u in G.nodes():
        for v in G.nodes():
            if u!= v and G.has_edge(u, v) and partition[u]!= partition[v]:
                Q.add_edge(partition[u], partition[v])

    return Q

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)])

    # Define a partition
    partition = {1: 'A', 2: 'A', 3: 'A', 4: 'B', 5: 'B', 6: 'B'}

    # Get the quotient graph
    Q = quotient_graph(G, partition)

    # Print the nodes and edges of the quotient graph
    print(Q.nodes())
    print(Q.edges())
