import networkx as nx

def create_prefix_tree(paths):
    G = nx.DiGraph()

    # Add nodes for each path
    for path in paths:
        G.add_node(path)

    # Add edges for prefix relationships
    for i in range(len(paths)):
        for j in range(i+1, len(paths)):
            if paths[i].startswith(paths[j][:-1]):
                G.add_edge(paths[i], paths[j])

    return G
