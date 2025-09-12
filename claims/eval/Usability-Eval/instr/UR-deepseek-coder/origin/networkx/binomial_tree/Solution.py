import networkx as nx

def binomial_tree(n):
    G = nx.Graph()
    nodes = [0]
    G.add_node(0)
    
    for i in range(1, n + 1):
        new_nodes = []
        for node in nodes:
            new_node = len(G)
            G.add_node(new_node)
            G.add_edge(node, new_node)
            new_nodes.append(new_node)
        nodes.extend(new_nodes)
    
    return G

# Example usage:
# n = 3
# tree = binomial_tree(n)
# print("Nodes:", tree.nodes())
# print("Edges:", tree.edges())
