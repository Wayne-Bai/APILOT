import networkx as nx
import numpy as np

def dual_barabasi_albert_graph(n, m):
    # Create an empty graph
    G = nx.Graph()
    
    # Add the initial nodes
    G.add_nodes_from(range(2 * m))
    
    # Connect the first m nodes
    for i in range(1, m):
        G.add_edge(i - 1, i)

    # Connect the first m nodes to the next m nodes
    for i in range(1, m):
        G.add_edge(m + i - 1, m + i)

    # Now add the remaining nodes
    for i in range(2 * m, n):
        G.add_node(i)
        
        # Create a list of targets based on degree
        targets = []
        
        # Calculate the degree of each node
        degree_sequence = np.array([G.degree(v) for v in G.nodes()])
        total_degree = np.sum(degree_sequence)
        
        for source in range(len(G.nodes())):
            if total_degree > 0:
                probability = degree_sequence[source] / total_degree
                targets.extend([source] * int(probability * 100))  # scaled probabilities
        
        # Select m unique targets
        chosen_targets = np.random.choice(targets, size=m, replace=False)
        
        # Create edges to chosen targets
        for target in chosen_targets:
            G.add_edge(i, target)

    return G

# Example usage:
n = 100  # total number of nodes
m = 2    # number of edges to attach from a new node to existing nodes

random_graph = dual_barabasi_albert_graph(n, m)
