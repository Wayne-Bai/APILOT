
import networkx as nx

def binomial_tree(n):
    # Create an empty graph
    G = nx.Graph()
    
    # Add the root node
    G.add_node('Root')
    
    # Recursively add nodes to the tree
    def add_nodes(parent, children):
        for child in children:
            G.add_edge(parent, child)
            add_nodes(child, G.neighbors(child))
    
    # Add the first level of nodes
    root = 'Root'
    for i in range(n):
        G.add_node(i + 1)
        G.add_edge(root, i + 1)
        add_nodes(i + 1, G.neighbors(i + 1))
    
    return G
