import networkx as nx

def create_graph_from_description(graph_description):
    """
    Create a small graph based on the provided description.

    Parameters:
    graph_description (list of tuples): Each tuple consists of two elements (node1, node2), defining an edge.

    Returns:
    nx.Graph: A NetworkX graph object created based on the graph description.
    """
    # Initialize an empty undirected graph
    G = nx.Graph()

    # Add edges to the graph based on the provided description
    for node1, node2 in graph_description:
        G.add_edge(node1, node2)

    return G

# Example usage
graph_description = [(1, 2), (2, 3), (3, 4), (4, 1)]  # Define the graph as a list of edges
graph = create_graph_from_description(graph_description)

# Display the edges of the graph to verify
print(list(graph.edges()))
