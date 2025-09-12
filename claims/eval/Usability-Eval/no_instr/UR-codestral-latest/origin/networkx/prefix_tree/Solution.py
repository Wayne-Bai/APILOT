import networkx as nx

def create_prefix_tree(paths):
    G = nx.DiGraph()

    for path in paths:
        node = ""
        for element in path:
            node += element
            if not G.has_node(node):
                G.add_node(node)
            if G.has_edge(node, "END"):
                G.remove_edge(node, "END")
            if path.index(element) != len(path) - 1:
                next_node = node + path[path.index(element) + 1]
                if not G.has_node(next_node):
                    G.add_node(next_node)
                if not G.has_edge(node, next_node):
                    G.add_edge(node, next_node)
            else:
                if not G.has_node("END"):
                    G.add_node("END")
                if not G.has_edge(node, "END"):
                    G.add_edge(node, "END")
    return G

# test
paths = [['A', 'B', 'C'], ['A', 'D'], ['E', 'D']]
G = create_prefix_tree(paths)
print(G.edges())  # to check the edges
