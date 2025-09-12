import networkx as nx

def create_directed_prefix_tree(paths):
    # Initialize a directed graph
    prefix_tree = nx.DiGraph()
    
    # Iterate through each path
    for path in paths:
        # Split the path into its components
        components = path.split('/')
        # Create edges for each pair of consecutive components
        for i in range(len(components)):
            if i == 0:
                # Add the root node
                prefix_tree.add_node(components[i])
            if i > 0:
                # Add the edge from the previous component to the current one
                prefix_tree.add_edge(components[i-1], components[i])
    
    return prefix_tree

# Example usage
paths = [
    "a/b/c",
    "a/b/d",
    "a/e/f",
    "g"
]
prefix_tree = create_directed_prefix_tree(paths)

# To visualize the tree, you might want to use:
# nx.draw(prefix_tree, with_labels=True, arrows=True)
