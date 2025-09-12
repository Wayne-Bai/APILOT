import networkx as nx

def has_eulerian_path(G, source=None):
    # Count the number of vertices with odd degree
    odd_degree_count = sum(1 for v in G.nodes() if G.degree[v] % 2 == 1)

    # Determine the conditions for having an Eulerian path
    if odd_degree_count == 0:
        return True  # Eulerian circuit exists
    elif odd_degree_count == 2 and source is not None:
        # If there are exactly two vertices with odd degree, and one of them is the source
        return source in G.nodes() and (G.degree[source] % 2 == 1)
    else:
        return False  # No Eulerian path exists

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(0, 1), (1, 2), (2, 0), (1, 3)])
# print(has_eulerian_path(G, source=1))
