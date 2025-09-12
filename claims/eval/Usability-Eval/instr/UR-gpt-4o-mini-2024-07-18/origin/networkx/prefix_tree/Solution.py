import networkx as nx

def create_directed_prefix_tree(paths):
    # Create a directed graph
    prefix_tree = nx.DiGraph()
    
    # Add edges to the graph for each path
    for path in paths:
        parts = path.split('/')
        for i in range(len(parts)):
            # Create a prefix by joining parts up to the current index
            prefix = '/'.join(parts[:i + 1])
            # Add an edge from the current prefix to the next part
            if i < len(parts) - 1:  # Avoid adding an edge for the last part
                prefix_tree.add_edge(prefix, '/'.join(parts[:i + 2]))
    
    return prefix_tree

# Example usage:
paths = [
    "home/user/documents",
    "home/user/music",
    "home/user/pictures",
    "home/admin/settings"
]

prefix_tree = create_directed_prefix_tree(paths)

# To visualize the prefix tree (optional)
import matplotlib.pyplot as plt

pos = nx.spring_layout(prefix_tree)
nx.draw(prefix_tree, pos, with_labels=True, arrows=True)
plt.show()
