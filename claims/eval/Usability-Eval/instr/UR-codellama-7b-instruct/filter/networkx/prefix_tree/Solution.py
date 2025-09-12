import networkx as nx

def create_prefix_tree(paths):
    """
    Creates a directed prefix tree from a list of paths.

    Parameters:
        paths (list): List of paths to be used for creating the prefix tree.

    Returns:
        networkx.DiGraph: Directed prefix tree with the given paths.
    """
    # Create an empty digraph to store the prefix tree
    g = nx.DiGraph()

    # Iterate over each path in the list
    for path in paths:
        # Get the current node and its neighbors
        curr_node = path[0]
        curr_neighbors = [path[-1]] if len(path) > 1 else []

        # Iterate over each neighbor of the current node
        for neighbor in curr_neighbors:
            # If the neighbor is not already in the graph, add it
            if neighbor not in g:
                g.add_node(neighbor)

            # Add an edge from the current node to its neighbor
            g.add_edge(curr_node, neighbor)

    return g