import networkx as nx

def create_graph_from_description(graph_description):
    """
    Create a graph based on the given description.

    Parameters:
    graph_description (dict): Dictionary containing nodes and edges.

    Returns:
    G (Graph): Generated NetworkX graph.
    """

    # Initialize an empty graph
    G = nx.Graph()

    # Add nodes to the graph
    nodes = graph_description.get("nodes", [])
    for node in nodes:
        G.add_node(node)

    # Add edges to the graph
    edges = graph_description.get("edges", [])
    for edge in edges:
        G.add_edge(*edge)

    return G

# Example usage:
graph_description = {
    "nodes": [1, 2, 3, 4],
    "edges": [(1, 2), (2, 3), (3, 4), (4, 1)]
}

graph = create_graph_from_description(graph_description)
# Now `graph` is a NetworkX Graph object.
