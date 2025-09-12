import networkx as nx

def create_directed_prefix_tree(paths):
    G = nx.DiGraph()  # create an empty directed graph

    # sort the paths by length, so we can add child nodes directly to parent nodes
    paths.sort(key=len)

    for path in paths:
        node = ""  # start at the root node
        for char in path:
            next_node = node + char  # the next node is the current node plus the current character
            if next_node not in G.nodes:
                G.add_edge(node, next_node)  # add an edge from the current node to the next node
            node = next_node  # move to the next node

    return G
