import networkx as nx # We first import the required networkx library

def quotient_graph(G, partition):
    # Input: G is a graph, partition is a dictionary that specifies the equivalence class for each node
    # Output: a graph H that is the quotient graph of G under the equivalence relation on nodes

    # Create the quotient graph
    H = nx.Graph()

    # Add nodes to the quotient graph
    H.add_nodes_from(partition.values())

    # Add edges to the quotient graph
    for u in G.nodes:
        for v in G.neighbors(u):
            if partition[u] != partition[v]: # Only add an edge if the nodes are in different equivalence classes
                H.add_edge(partition[u], partition[v])

    return H
