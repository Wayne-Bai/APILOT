import networkx as nx

def create_prefix_tree(paths):
    G = nx.DiGraph()

    for path in paths:
        node = G.add_node(path)
        for i, char in enumerate(path):
            if i == len(path) - 1:
                G.add_edge(node, path)
            else:
                G.add_edge(node, path[i+1:])

    return G
