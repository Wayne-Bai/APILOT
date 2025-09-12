import networkx as nx

def has_eulerian_path(G, source=None):
    # Function to check if the graph G has an Eulerian path
    
    # First, we check if G is empty
    if G.is_empty():
        return True

    # Check the degrees of all nodes
    odd_degree_nodes = [node for node, degree in G.degree() if degree % 2 == 1]

    # Conditions for having an Eulerian path
    if source is None:
        # Either 0 or 2 vertices have odd degree
        return len(odd_degree_nodes) in [0, 2]
    else:
        # If source is specified, check that it has odd degree and exactly one other node has an odd degree
        if source not in G:
            raise ValueError("The source node is not in the graph.")
        return (len(odd_degree_nodes) == 2 and G.degree(source) % 2 == 1 and source in odd_degree_nodes)

# Example usage:
G = nx.Graph([(0, 1), (1, 2), (2, 3), (3, 0), (1, 3)])
print(has_eulerian_path(G))  # Should print True if the graph has an Eulerian path

# If checking with a source:
print(has_eulerian_path(G, source=0))  # Whether there's an Eulerian path starting at node 0
