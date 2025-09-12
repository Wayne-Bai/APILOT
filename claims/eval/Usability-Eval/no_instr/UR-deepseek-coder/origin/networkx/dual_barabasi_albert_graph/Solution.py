import networkx as nx
import random

def dual_barabasi_albert_graph(n, m1, m2, p):
    """
    Returns a random graph using dual Barabási–Albert preferential attachment.

    Parameters:
    n (int): Number of nodes.
    m1 (int): Number of edges to attach from a new node to existing nodes for the first model.
    m2 (int): Number of edges to attach from a new node to existing nodes for the second model.
    p (float): Probability of choosing the first model.

    Returns:
    G (networkx.Graph): The generated graph.
    """
    G = nx.empty_graph(m1 + m2)
    
    # Initialize the degree dictionary
    degree_dict = {node: 0 for node in G.nodes()}
    
    # Add initial edges to the graph
    for i in range(m1 + m2):
        for j in range(i + 1, m1 + m2):
            G.add_edge(i, j)
            degree_dict[i] += 1
            degree_dict[j] += 1
    
    # Add remaining nodes with preferential attachment
    for new_node in range(m1 + m2, n):
        if random.random() < p:
            # Use the first model
            total_degree = sum(degree_dict.values())
            targets = set()
            while len(targets) < m1:
                # Preferential attachment
                target = random.choices(list(degree_dict.keys()), weights=list(degree_dict.values()))[0]
                if target not in targets:
                    targets.add(target)
            for target in targets:
                G.add_edge(new_node, target)
                degree_dict[new_node] += 1
                degree_dict[target] += 1
        else:
            # Use the second model
            total_degree = sum(degree_dict.values())
            targets = set()
            while len(targets) < m2:
                # Preferential attachment
                target = random.choices(list(degree_dict.keys()), weights=list(degree_dict.values()))[0]
                if target not in targets:
                    targets.add(target)
            for target in targets:
                G.add_edge(new_node, target)
                degree_dict[new_node] += 1
                degree_dict[target] += 1
    
    return G

# Example usage:
# G = dual_barabasi_albert_graph(100, 2, 3, 0.5)
