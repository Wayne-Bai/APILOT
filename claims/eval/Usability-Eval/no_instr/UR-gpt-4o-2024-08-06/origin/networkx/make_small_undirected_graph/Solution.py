import networkx as nx

def create_graph_from_description(graph_description):
    """
    Create and return a small undirected graph
    based on the provided graph description.

    graph_description: A list of tuples where each tuple represents an edge
                       (node1, node2). Nodes can be of any immutable type.
    """
    G = nx.Graph()  # Create an empty undirected graph
    G.add_edges_from(graph_description)  # Add edges from the graph description

    return G

# Example usage:
graph_description = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]
graph = create_graph_from_description(graph_description)

# Display the graph structure
for edge in graph.edges:
    print(edge)
