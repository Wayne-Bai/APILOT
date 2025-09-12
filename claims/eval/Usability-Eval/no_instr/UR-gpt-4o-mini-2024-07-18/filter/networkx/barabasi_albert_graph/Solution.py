import networkx as nx

def generate_random_barabasi_albert_graph(n, m):
    """
    Generate a random graph using the Barabási–Albert preferential attachment model.
    
    Parameters:
    n (int): The total number of nodes.
    m (int): The number of edges to attach from a new node to existing nodes.
    
    Returns:
    G (networkx.Graph): The generated graph.
    """
    G = nx.barabasi_albert_graph(n, m)
    return G

# Example usage
if __name__ == "__main__":
    num_nodes = 100  # Total number of nodes
    edges_to_attach = 2  # Number of edges to attach from new nodes
    random_graph = generate_random_barabasi_albert_graph(num_nodes, edges_to_attach)
    print(nx.info(random_graph))
