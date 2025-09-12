import networkx as nx

def minimum_weight_maximal_matching(G):
    # Compute the maximal matching with the minimum weight
    matching = nx.max_weight_matching(G, maxcardinality=True, weight='weight')
    return matching

# Example usage:
# Create a graph
G = nx.Graph()

# Add edges along with their weights
G.add_edge(1, 2, weight=3)
G.add_edge(2, 3, weight=1)
G.add_edge(3, 4, weight=2)
G.add_edge(1, 4, weight=4)
G.add_edge(2, 4, weight=5)

# Compute the minimum-weight maximal matching
matching = minimum_weight_maximal_matching(G)

# Output the matching
print("Minimum-weight maximal matching:", matching)
