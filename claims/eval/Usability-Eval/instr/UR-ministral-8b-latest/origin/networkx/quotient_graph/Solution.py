import networkx as nx

def quotient_graph(G, equivalence_relation):
    """
    Returns the quotient graph of G under the specified equivalence relation on nodes.

    Parameters:
    G (networkx.Graph): The original graph.
    equivalence_relation (function): A function that takes two nodes and returns True if they are in the same equivalence class.

    Returns:
    networkx.Graph: The quotient graph.
    """
    quotient = nx.Graph()

    # Initialize dictionary to hold representative nodes
    rep_nodes = {}

    for node in G.nodes():
        # Find a node in the same equivalence class
        for rep_node in rep_nodes:
            if equivalence_relation(node, rep_node):
                break
        else:
            rep_node = node

        # Add representative node to the quotient graph
        rep_nodes[rep_node] = True

    for node in rep_nodes:
        quotient.add_node(node)

    for u, v in G.edges():
        # Find representative nodes for u and v
        u_rep = next((k for k in rep_nodes if equivalence_relation(u, k)), u)
        v_rep = next((k for k in rep_nodes if equivalence_relation(v, k)), v)

        # Add edge to quotient graph
        quotient.add_edge(u_rep, v_rep)

    return quotient

# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 3)])

    # Define an equivalence relation
    def equivalence_relation(u, v):
        # Example: Equivalent if u and v are non-equal
        return u == v

    # Get the quotient graph
    quotient_graph = quotient_graph(G, equivalence_relation)

    # Print the quotient graph
    print(quotient_graph.edges())
