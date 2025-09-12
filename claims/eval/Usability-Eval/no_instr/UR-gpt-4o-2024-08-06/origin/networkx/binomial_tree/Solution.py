import networkx as nx

def binomial_tree(n):
    """Returns the Binomial Tree of order n."""
    if n < 0:
        raise ValueError("Order n must be a non-negative integer.")
    
    G = nx.Graph()
    
    # Start with a single node
    G.add_node(0)
    
    for i in range(n):
        H = G.copy()
        mapping = {v: v + len(G) for v in H.nodes()}
        H = nx.relabel_nodes(H, mapping)
        G.add_edges_from(H.edges())
        G.add_edge(0, len(G))
        G.add_nodes_from(H.nodes())
    
    return G

# Example of how to use the function
n = 3
binomial_tree_graph = binomial_tree(n)
print("Nodes:", binomial_tree_graph.nodes())
print("Edges:", binomial_tree_graph.edges())
