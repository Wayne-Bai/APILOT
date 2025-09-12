
import networkx as nx

def create_directed_prefix_tree(paths):
    tree = nx.DiGraph()
    for path in paths:
        tree.add_path(path)
    return tree
