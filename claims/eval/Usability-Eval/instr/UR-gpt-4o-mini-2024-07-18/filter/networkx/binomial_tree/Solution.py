import networkx as nx

def binomial_tree(n):
    """Create a binomial tree of order n and return it as a NetworkX graph."""
    G = nx.Graph()
    
    # Number of nodes in a binomial tree of order n
    num_nodes = 2 ** n
    
    # Add nodes to the graph
    G.add_nodes_from(range(num_nodes))
    
    # Create edges for the binomial tree
    def add_edges(k):
        if k == 0:
            return
        num_nodes_k = 2 ** k
        for i in range(num_nodes_k // 2):
            G.add_edge(i, i + num_nodes_k // 2)
        add_edges(k - 1)

    add_edges(n)
    
    return G

# Example Usage
tree = binomial_tree(3)
print("Nodes:", tree.nodes())
print("Edges:", tree.edges())
