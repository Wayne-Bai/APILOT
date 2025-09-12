
# Importing the necessary libraries
import networkx as nx

def add_path_to_prefix_tree(tree, path):
    current_node = tree
    for node in path:
        if node not in current_node:
            current_node[node] = {}
        current_node = current_node[node]

def build_prefix_tree(paths):
    prefix_tree = {}
    for path in paths:
        add_path_to_prefix_tree(prefix_tree, path)
    return prefix_tree

# List of paths
paths = [
    ['a', 'b', 'c'],
    ['a', 'b', 'd'],
    ['a', 'e', 'f'],
    ['g'],
    ['g', 'h']
]

# Creating the directed prefix tree
prefix_tree = build_prefix_tree(paths)

# Displaying the directed prefix tree
print(prefix_tree)
