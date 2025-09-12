
import networkx as nx

def create_directed_prefix_tree(paths):
    """
    Creates a directed prefix tree from a list of paths.
    
    :param paths: A list of paths to be added to the tree
    :type paths: List[str]
    :return: The directed prefix tree
    :rtype: nx.DiGraph
    """
    # Create an empty graph
    g = nx.DiGraph()
    
    # Add each path to the graph
    for path in paths:
        # Split the path into its components
        parts = path.split("/")
        
        # Add each part of the path as a node in the graph
        for i, part in enumerate(parts):
            g.add_node(part)
            
            # If this is not the last part of the path, add an edge from this node to the next part
            if i < len(parts) - 1:
                g.add_edge(part, parts[i + 1])
    
    return g
