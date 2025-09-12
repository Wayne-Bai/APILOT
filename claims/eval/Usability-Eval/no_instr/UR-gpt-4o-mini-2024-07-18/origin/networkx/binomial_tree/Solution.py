import networkx as nx

def binomial_tree(n):
    """Returns the Binomial Tree of order n."""
    if n < 0:
        raise ValueError("Order must be a non-negative integer")

    # Create a new directed graph
    B_n = nx.DiGraph()

    # Function to recursively add nodes and edges
    def add_binomial_tree(order, node):
        if order == 0:
            B_n.add_node(node)
            return

        # Add the current node
        B_n.add_node(node)

        # Recursively add the left and right subtrees
        left_child = f"{node}0"
        right_child = f"{node}1"
        
        # Add edges to the children
        B_n.add_edge(node, left_child)
        B_n.add_edge(node, right_child)

        add_binomial_tree(order - 1, left_child)
        add_binomial_tree(order - 1, right_child)

    add_binomial_tree(n, 'B')

    return B_n

# Example usage:
# Create a binomial tree of order 3
binomial_tree_order_3 = binomial_tree(3)
print(binomial_tree_order_3.nodes)
print(binomial_tree_order_3.edges)
