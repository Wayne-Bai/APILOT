import networkx as nx

def build_prefix_tree(paths):
    """
    Build a directed prefix tree from a list of paths.
    
    Parameters:
    paths (list of list of str): A list where each element is a list representing a path.

    Returns:
    nx.DiGraph: A directed graph representing the prefix tree.
    """
    tree = nx.DiGraph()
    for path in paths:
        current_node = 'root'  # Starting at root node
        for element in path:
            next_node = f"{current_node}/{element}"
            if not tree.has_node(next_node):
                tree.add_node(next_node, label=element)
            if not tree.has_edge(current_node, next_node):
                tree.add_edge(current_node, next_node)
            current_node = next_node
    return tree


# Example usage
paths = [
    ['home', 'about'],
    ['home', 'products', 'item1'],
    ['home', 'products', 'item2'],
    ['home', 'contact'],
]

prefix_tree = build_prefix_tree(paths)

# Optionally, you can print nodes and edges to verify
print("Nodes:")
print(prefix_tree.nodes(data=True))
print("\nEdges:")
print(list(prefix_tree.edges()))
