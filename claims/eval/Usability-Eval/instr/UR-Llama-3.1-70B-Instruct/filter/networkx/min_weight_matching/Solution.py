import networkx as nx
import matplotlib.pyplot as plt

def min_weight_maximal_matching(G):
    # Sort edges by weight
    edges = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])

    # Initialize an empty matching
    matching = nx.Graph()

    for u, v, data in edges:
        if not matching.has_node(u) and not matching.has_node(v):
            matching.add_edge(u, v, weight=data['weight'])

    return matching

# Create a new graph
G = nx.Graph()

# Add edges with weights
G.add_edge(1, 2, weight=1)
G.add_edge(1, 3, weight=4)
G.add_edge(2, 3, weight=2)
G.add_edge(2, 4, weight=3)
G.add_edge(3, 4, weight=5)

# Compute the minimum-weight maximal matching
matching = min_weight_maximal_matching(G)

# Print the edges of the matching
print("Edges of the minimum-weight maximal matching:")
for u, v in matching.edges():
    print(f"({u}, {v})")

# Draw the graph and the matching
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw(matching, pos, edge_color='r', with_labels=True)
plt.show()
