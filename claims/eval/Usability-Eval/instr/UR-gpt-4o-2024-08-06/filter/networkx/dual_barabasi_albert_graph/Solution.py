import networkx as nx
import random

def dual_barabasi_albert_graph(n, m1, m2, p):
    """
    Generate a random graph using a dual Barabási–Albert preferential attachment model.

    Parameters:
    n : int
        Number of nodes
    m1 : int
        Number of edges to attach from a new node to existing nodes using probability p
    m2 : int
        Number of edges to attach from a new node to existing nodes using probability (1-p)
    p : float
        Probability of using m1 edges during attachment
    
    Returns:
    G : Graph
        A dual Barabási–Albert preferential attachment graph
    """
    if m1 < 1 or m1 >= n or m2 < 1 or m2 >= n:
        raise nx.NetworkXError(f"m1 and m2 must satisfy 1 <= m1 < n and 1 <= m2 < n, but got m1={m1}, m2={m2}.")
    if not (0 <= p <= 1):
        raise nx.NetworkXError(f"p must be a probability: 0 <= p <= 1, but got p={p}.")
    
    G = nx.complete_graph(m1 + m2)
    while len(G) < n:
        # Choose number of edges to attach based on probability p
        if random.random() < p:
            num_edges = m1
        else:
            num_edges = m2
            
        # Create new node and preferentially attach edges
        new_node = len(G)
        targets = _random_select(G, num_edges)
        G.add_node(new_node)
        G.add_edges_from((new_node, target) for target in targets)

    return G

def _random_select(G, num_edges):
    """Selects `num_edges` nodes from `G` with probability proportional to node degree."""
    node_list = []
    degree_sum = sum(d for n, d in G.degree())
    
    for node, degree in G.degree():
        node_probability = degree / degree_sum
        node_list.extend([node] * int(node_probability * 100))  # Extend list by proportional probability

    return random.sample(node_list, num_edges)

# Example usage
graph = dual_barabasi_albert_graph(n=100, m1=2, m2=3, p=0.5)
