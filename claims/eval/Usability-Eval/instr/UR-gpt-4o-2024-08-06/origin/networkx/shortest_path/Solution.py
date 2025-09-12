import networkx as nx

def compute_shortest_paths(graph, source):
    """
    Computes the shortest paths from the source node to all other nodes in the given graph
    using Dijkstra's algorithm.

    Parameters:
    - graph: A networkx graph object
    - source: The node from which shortest paths are to be calculated

    Returns:
    A dictionary with the target node as the key and the shortest path as the value.
    """
    return nx.single_source_dijkstra_path(graph, source)

# Example usage:
# Create a sample graph
G = nx.Graph()
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'D', weight=1)
G.add_edge('C', 'D', weight=5)
G.add_edge('B', 'E', weight=2)
G.add_edge('D', 'E', weight=1)

# Compute the shortest paths from node 'A'
shortest_paths = compute_shortest_paths(G, 'A')
print(shortest_paths)
