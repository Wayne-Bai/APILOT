
import networkx as nx

def has_eulerian_path(G, source=None):
    def is_connected(G):
        return len(list(nx.connected_components(G))) == 1
    
    if not is_connected(G):
        return False
    
    odd_degree_nodes = [node for node, degree in G.degree() if degree % 2 != 0]
    
    if len(odd_degree_nodes) not in [0, 2]:
        return False
    
    return True

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
print(has_eulerian_path(G))
