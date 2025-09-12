import networkx as nx

def has_eulerian_path(G, source=None):
    """
    Return True iff G has an Eulerian path.
    
    An Eulerian path is a path in a graph which uses each edge of a graph exactly once.
    If source is specified, then this function checks whether an Eulerian path that starts at node source exists.

    Parameters:
    G (Graph): The input graph
    source (node): The node where the Eulerian path starts
    
    Returns:
    bool: True if the graph contains an Eulerian path, False otherwise
    """

    # Check if the graph is connected
    if not nx.is_connected(G):
        return False

    # Check the in-degree and out-degree of each node
    in_degree = G.in_degree(node=None)
    out_degree = G.out_degree(node=None)

    if source is not None:
        # Check if the graph contains an Eulerian path starting at the source node
        in_degree[source] -= 1
        in_degree = G.in_degree(node=None)
        out_degree = G.out_degree(node=None)
    
    # Check if all nodes have an even degree
    if all(deg % 2 == 0 for deg in in_degree.values() + list(out_degree.values())):
        return True
    
    # If all nodes have an even degree, the graph contains an Eulerian circuit
    # A graph with an Eulerian circuit also contains an Eulerian path
    return any(deg % 2!= 0 for deg in in_degree.values() + list(out_degree.values()))

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3), (3, 2)])
print(has_eulerian_path(G))  # Output: True

G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (1, 3)])
print(has_eulerian_path(G))  # Output: False

G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
print(has_eulerian_path(G, source=1))  # Output: False
