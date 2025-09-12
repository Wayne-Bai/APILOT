import networkx as nx

def create_prefix_tree(paths):
    G = nx.DiGraph()
    
    for path in paths:
        for i in range(len(path) - 1):
            if not G.has_edge(path[i], path[i + 1]):
                G.add_edge(path[i], path[i + 1])
    
    return G

# Example usage:
paths = [
    ['A', 'B', 'C'],
    ['A', 'B', 'D'],
    ['A', 'E']
]

prefix_tree = create_prefix_tree(paths)
print("Nodes:", prefix_tree.nodes())
print("Edges:", prefix_tree.edges())
