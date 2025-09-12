import networkx as nx

# Generate a Barabási-Albert graph
def generate_barabasi_albert_graph(n, m):
    """
    Generates a random graph using the Barabási-Albert (BA) preferential attachment model.
    
    Parameters:
    n (int): Number of nodes
    m (int): Number of edges to attach from a new node to existing nodes

    Returns:
    G (networkx.Graph): A networkx graph instance of the Barabási-Albert model
    """
    G = nx.barabasi_albert_graph(n, m)
    return G

# Example usage
ba_graph = generate_barabasi_albert_graph(50, 2)
print(nx.info(ba_graph))
