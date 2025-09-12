import networkx as nx

def return_small_graph(graph_description):
    """
    Return the small graph described by graph_description.

    Parameters
    ----------
    graph_description : dict
        Dictionary describing the graph structure.

    Returns
    -------
    G : networkx.Graph
        The constructed graph.
    """

    # Initialize an empty graph
    G = nx.Graph()

    # Get the nodes and edges from the graph description
    nodes = graph_description.get('nodes', [])
    edges = graph_description.get('edges', [])

    # Add nodes to the graph
    G.add_nodes_from(nodes)

    # Add edges to the graph
    G.add_edges_from(edges)

    return G

# Example usage:

# Define the graph description
graph_description = {
    'nodes': [1, 2, 3],
    'edges': [(1, 2), (2, 3), (3, 1)]
}

# Create the graph
G = return_small_graph(graph_description)

# Print the graph details
print("Nodes: ", G.nodes())
print("Edges: ", G.edges())

for node in G.nodes():
    print("Degree of node", node, ":", G.degree(node))
