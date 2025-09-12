import networkx as nx
import numpy as np

def barabasi_albert_graph(n, m):
    """
    Returns a random graph using dual Barabási–Albert preferential attachment.

    Parameters:
    n (int): The number of nodes in the graph.
    m (int): The number of edges each new node adds.

    Returns:
    G: A new Graph object.
    """
    G = nx.Graph()
    G.add_node(0)  # Start with one node

    for i in range(1, n):
        G.add_node(i)
        
        # Select m+1 nodes from existing nodes (with their degrees)
        nodes = list(G.nodes)
        weights = [deg for _, deg in G.degree(nodes)]
        
        # Select m nodes from the nodes above (with their lengths), plus the current node
        new_nodes = np.random.choice(nodes, size=m+1, replace=False, p=weights/np.sum(weights))
        new_nodes = [new_nodes.tolist(), new_nodes[:m].tolist()]
        
        # Add edges to the new node from all selected nodes
        for j in new_nodes[0]:
            G.add_edge(i, j)
        
        # Add m edges from the new node to other selected nodes
        other_nodes = [n for n in new_nodes[0] if n!= i]
        other_nodes.extend(new_nodes[1])
        
        G.add_edges_from([(i, k) for k in np.random.choice(other_nodes, size=m, replace=False)])

    return G

# Example usage:
n = 100
m = 3
G = barabasi_albert_graph(n, m)
nx.draw(G, with_labels=True)
