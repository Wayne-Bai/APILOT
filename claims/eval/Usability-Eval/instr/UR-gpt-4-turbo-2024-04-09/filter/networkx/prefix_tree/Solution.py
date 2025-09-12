import networkx as nx

def create_prefix_tree(paths):
    tree = nx.DiGraph()
    for path in paths:
        current_node = 0  # Start from the root node
        for part in path:
            # Check if the node part exists
            if not tree.has_node(part):
                tree.add_node(part)
            if not tree.has_edge(current_node, part):
                tree.add_edge(current_node, part)
            current_node = part
    return tree

# Example usage with sample paths
paths = [
    ["root", "child1", "child2"],
    ["root", "child3"],
    ["root", "child1", "child4"]
]

prefix_tree = create_prefix_tree(paths)

# Print the edges of the tree
print(list(prefix_tree.edges()))
