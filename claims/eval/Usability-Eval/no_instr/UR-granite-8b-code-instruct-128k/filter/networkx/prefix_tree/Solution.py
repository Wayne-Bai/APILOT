import networkx as nx

def create_directed_prefix_tree(paths):
    G = nx.DiGraph()
    for path in paths:
        current_node = G
        for label in path:
            if label not in current_node:
                current_node[label] = {}
            current_node = current_node[label]
    return G
