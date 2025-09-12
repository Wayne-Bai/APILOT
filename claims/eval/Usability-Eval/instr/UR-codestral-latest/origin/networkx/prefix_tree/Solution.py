import networkx as nx

def create_prefix_tree(paths):
    G = nx.DiGraph()

    for path in paths:
        for i in range(len(path)):
            prefix = path[:i+1]
            # Add node for prefix if it doesn't exist
            if prefix not in G:
                G.add_node(prefix)
            # Add edge from parent prefix to this prefix if it doesn't exist
            if i > 0:
                parent_prefix = path[:i]
                if not G.has_edge(parent_prefix, prefix):
                    G.add_edge(parent_prefix, prefix)

    return G
