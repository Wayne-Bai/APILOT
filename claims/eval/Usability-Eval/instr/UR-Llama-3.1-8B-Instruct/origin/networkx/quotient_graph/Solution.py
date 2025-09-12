import networkx as nx
import matplotlib.pyplot as plt

def equivalence_class_quotient(G, relation):
    """
    Returns the quotient graph of G under the specified equivalence relation on nodes.

    Args:
    G (nx.Graph): The input graph.
    relation (dict): A dictionary where each key is a node in G, and its value is a list of nodes that are equivalent to it.

    Returns:
    nx.Graph: The quotient graph of G.
    """

    # Initialize quotient graph as an empty graph
    Q = nx.Graph()

    # Map each equivalence class to a node in the quotient graph
    class_map = {}
    for node in relation:
        if relation[node] not in class_map.keys():
            class_map[relation[node]] = len(Q.nodes)

    # Add nodes to the quotient graph
    for nodes in class_map.values():
        Q.add_node(nodes)

    # Add edges to the quotient graph
    for node in G.nodes:
        # Get the equivalence class of the current node
        for key in class_map:
            if node in key:
                for neighbor in G.neighbors(node):
                    # Get the equivalence class of the neighbor
                    for key2 in class_map:
                        if neighbor in key2:
                            # Add an edge to the quotient graph if there was an edge in the original graph
                            if class_map[key]!= class_map[key2] and G.has_edge(node, neighbor):
                                Q.add_edge(class_map[key], class_map[key2])

    return Q


# Example usage
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)])

relation = {1: [1, 4], 2: [2, 4], 3: [3]}

Q = equivalence_class_quotient(G, relation)

# Visualize the quotient graph
pos = nx.spring_layout(Q)
nx.draw_networkx_nodes(Q, pos)
nx.draw_networkx_edges(Q, pos, width=2)
nx.draw_networkx_labels(Q, pos)

plt.show()
