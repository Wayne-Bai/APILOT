import networkx as nx

def generate_binomial_tree(n):
    if n <= 0:
        return []

    tree = nx.Graph()
    tree.add_node(0)

    for i in range(1, n + 1):
        for node in tree.nodes():
            tree.add_node(2 * node)
            tree.add_node(2 * node + 1)
            tree.add_edge(node, 2 * node)
            tree.add_edge(node, 2 * node + 1)

    return tree
