import networkx as nx
import os
import pathlib

def create_prefix_tree(paths):
    """
    Creates a directed prefix tree from a list of paths.

    Args:
        paths (list): A list of paths.

    Returns:
        nx.DiGraph: A directed prefix tree represented as a Digraph.
    """
    # Create an empty directed graph
    G = nx.DiGraph()

    # Iterate over each path in the list
    for path in paths:
        # Split the path into components (directories and filename)
        components = path.split(os.sep)
        
        # Add each component as a node in the graph
        for i, component in enumerate(components):
            node_name = component
            if G.has_node(node_name):
                continue
            else:
                G.add_node(node_name)
            
            # Add a directed edge from the current node to the next node in the path
            if i < len(components) - 1:
                G.add_edge(node_name, components[i + 1])

    return G

# Example usage
paths = ['/path/to/file1.txt', '/path/to/file2.txt', '/path/to/directory/subfile.txt']
G = create_prefix_tree(paths)

# Print the edges of the graph (i.e., the prefix tree)
print("Edges:", G.edges)

# Print the nodes of the graph (i.e., the directories and files)
print("Nodes:", G.nodes)
