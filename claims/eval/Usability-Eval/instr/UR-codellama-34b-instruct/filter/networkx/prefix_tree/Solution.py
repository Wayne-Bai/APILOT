
import networkx as nx
from collections import defaultdict

def create_prefix_tree(paths):
    """
    Creates a directed prefix tree from a list of paths.

    The prefix tree is represented as a dictionary, where each key is a node in the tree and the corresponding value is a list of child nodes.

    Each path in the input list is added to the tree by starting at the root node and recursively adding child nodes for each element in the path. If a child node already exists, it is reused instead of creating a new one.

    The resulting prefix tree can be used for various tasks such as finding all paths that start with a given prefix or finding the longest common prefix between two paths.

    Args:
        paths (list): A list of paths to add to the prefix tree. Each path should be a list of strings.

    Returns:
        dict: The prefix tree represented as a dictionary.
    """
    root = {}
    for path in paths:
        current_node = root
        for element in path:
            if element not in current_node:
                current_node[element] = {}
            current_node = current_node[element]
    return root
