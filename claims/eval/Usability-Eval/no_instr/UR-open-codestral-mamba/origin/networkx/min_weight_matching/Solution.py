import networkx as nx

def max_weight_maximal_matching(G):
    # Calculate the maximum weighted matching in the graph G
    matching = nx.max_weight_matching(G)

    # Convert the matching to a list of edges
    edges = list(matching)

    # Convert the edges to a set of nodes
    nodes = set([node for edge in edges for node in edge])

    # Find the most heavy node in G
    heaviest_node = max(nodes, key=G.degree)

    # Add the heaviest node to the matching
    edges.append((heaviest_node,))

    # Return the maximum weight maximal matching
    return edges

# Create a graph
G = nx.Graph()

# Add edges with weights
G.add_edge('A', 'B', weight=5)
G.add_edge('B', 'C', weight=3)
G.add_edge('A', 'D', weight=8)
G.add_edge('D', 'E', weight=2)
G.add_edge('D', 'F', weight=6)

# Compute the maximum weight maximal matching
matching = max_weight_maximal_matching(G)
print(matching)
