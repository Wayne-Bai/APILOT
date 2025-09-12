import networkx as nx

def binomial_tree(n):
    if n < 0:
        raise ValueError("Order of binomial tree must be non-negative")
    
    G = nx.Graph()
    
    # Base case for order 0
    if n == 0:
        G.add_node(0)
        return G
    
    # Combine two binomial trees of order n-1
    T_prev = binomial_tree(n - 1)
    G = nx.disjoint_union(T_prev, T_prev)
    
    # Connect the roots of the two binomial trees to form a binomial tree of order n
    root_old = 2 ** (n - 1) - 1
    root_new = root_old + 1
    G.add_edge(root_old, root_new)
    
    return G

# Example usage for a binomial tree of order 3
order = 3
tree = binomial_tree(order)
print(f"Nodes in the binomial tree of order {order}:", tree.nodes())
print(f"Edges in the binomial tree of order {order}:", tree.edges())
