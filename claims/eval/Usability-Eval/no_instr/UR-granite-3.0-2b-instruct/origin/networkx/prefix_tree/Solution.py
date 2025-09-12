import networkx as nx

def create_directed_prefix_tree(paths):
    G = nx.DiGraph()

    for path in paths:
        parent = G.nodes[path[0]]['parent']
        for i in range(1, len(path)):
            child = G.nodes[path[i]]['child']
            if child is None:
                G.add_edge(parent, path[i])
            else:
                G.add_edge(parent, child)
                G.nodes[child]['parent'] = parent

    return G
