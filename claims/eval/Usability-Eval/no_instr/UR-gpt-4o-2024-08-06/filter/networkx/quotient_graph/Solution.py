import networkx as nx

def quotient_graph(G, node_equivalence, edge_relation=None):
    """
    Returns the quotient graph of G under the specified equivalence relation on nodes.
    
    Parameters:
    G (nx.Graph): The original graph.
    node_equivalence (function): A function that takes two nodes u and v and returns True if
                                 they are equivalent under the relation, otherwise False.
    edge_relation (function): A function that takes two edges (u, v) and (x, y) and returns True
                              if the edges are equivalent under the relation, otherwise False.
    
    Returns:
    nx.Graph: The quotient graph.
    """

    # Create a dictionary to determine node equivalence class
    equivalence_classes = {}
    for node in G.nodes():
        for eq_class in equivalence_classes.values():
            if node_equivalence(next(iter(eq_class)), node):
                eq_class.add(node)
                break
        else:
            equivalence_classes[frozenset([node])] = {node}

    # Create a new graph for the quotient graph
    Q = nx.Graph()

    # Add nodes representing equivalence classes
    for eq_class in equivalence_classes.values():
        Q.add_node(frozenset(eq_class))

    # Add edges based on equivalence classes and edge relation
    for u, v in G.edges():
        u_class = next(eq_class for eq_class in equivalence_classes.values() if u in eq_class)
        v_class = next(eq_class for eq_class in equivalence_classes.values() if v in eq_class)
        
        if u_class != v_class:
            if not edge_relation or edge_relation(u, v, u_class, v_class):
                Q.add_edge(frozenset(u_class), frozenset(v_class))
    
    return Q

# Example usage:
# Define the node equivalence relation
def node_equivalence(u, v):
    return u % 2 == v % 2  # Example: nodes are equivalent if they have the same parity

# Example graph
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])

# Compute the quotient graph
Q = quotient_graph(G, node_equivalence)

# Visualize the quotient graph
import matplotlib.pyplot as plt
nx.draw(Q, with_labels=True)
plt.show()
