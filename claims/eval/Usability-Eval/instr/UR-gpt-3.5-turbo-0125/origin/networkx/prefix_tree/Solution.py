
import networkx as nx

def create_prefix_tree(paths):
    G = nx.DiGraph()
    
    for path in paths:
        current_node = ""
        
        for node in path:
            current_node += node
            
            if not G.has_node(current_node):
                G.add_node(current_node)
            
            if current_node != node:
                G.add_edge(current_node[:-1], current_node)
                
    return G

# Example paths
paths = [["a", "b", "c"], ["a", "b", "d"], ["a", "e", "f"]]
prefix_tree = create_prefix_tree(paths)

print("Nodes in the prefix tree:", prefix_tree.nodes)
print("Edges in the prefix tree:", prefix_tree.edges)
