import networkx as nx

def generate_barabasi_albert_graph(n, m):
    """
    Generates a random graph using Barabási–Albert preferential attachment model.
    
    Parameters:
    n (int): Number of nodes in the graph.
    m (int): Number of edges to attach from a new node to existing nodes.
    
    Returns:
    G (networkx.Graph): A graph generated using the Barabási–Albert model.
    """
    G = nx.barabasi_albert_graph(n, m)
    return G

# Example usage:
n = 100  # Number of nodes
m = 2    # Number of edges for new node
graph = generate_barabasi_albert_graph(n, m)
