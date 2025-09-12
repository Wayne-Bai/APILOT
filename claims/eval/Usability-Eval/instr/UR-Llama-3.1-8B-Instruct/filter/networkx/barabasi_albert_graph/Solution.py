import networkx as nx
import random

def barabasi_albert_graph(n, m):
    """
    Returns a random graph using Barabási–Albert preferential attachment.
    
    Parameters:
    n (int): The number of nodes in the graph.
    m (int): The number of edges for each new node to connect to.
    
    Returns:
    G (nx.Graph): The generated graph.
    """
    G = nx.Graph()
    # Initialize the graph with m nodes
    G.add_nodes_from(range(m))
    
    # Add nodes one by one
    for _ in range(n - m):
        new_node = n - m + _
        # Select m nodes with degree
        current_degrees = [G.degree(node) for node in G.nodes]
        probabilities = [degree / sum(current_degrees) for degree in current_degrees]
        # Select nodes using weighted random choice based on probabilities
        new_edges = random.choices(list(G.nodes), weights=probabilities, k=m)
        
        for edge in new_edges:
            if (new_node, edge) not in G.edges and (edge, new_node) not in G.edges:
                G.add_edge(new_node, edge)
        
        G.add_node(new_node)
    
    return G

# Usage example
G = barabasi_albert_graph(100, 5)
print(nx.info(G))
