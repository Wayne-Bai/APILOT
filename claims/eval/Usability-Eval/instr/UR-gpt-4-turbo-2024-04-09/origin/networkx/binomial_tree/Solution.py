import networkx as nx

def binomial_tree(n):
    B = nx.Graph()
    for i in range(n):
        nodes = list(B.nodes)
        # Each iteration, add 2^i new nodes
        for j in range(2 ** i):
            current_label = len(B)
            B.add_node(current_label)
            if nodes:
                # Connect new node to corresponding node from previous generation
                parent = nodes[j // 2]
                B.add_edge(parent, current_label)
    return B

# Example: Create a Binomial Tree of order 3
bt = binomial_tree(3)
print(bt.edges())
