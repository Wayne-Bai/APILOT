import networkx as nx

def compute_extreme_distance(G):
    diameter = nx.diameter(G)
    radius = nx.radius(G)
    return {'diameter': diameter, 'radius': radius}

# Example usage
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)
print(compute_extreme_distance(G))  # Output: {'diameter': 3, 'radius': 2}
