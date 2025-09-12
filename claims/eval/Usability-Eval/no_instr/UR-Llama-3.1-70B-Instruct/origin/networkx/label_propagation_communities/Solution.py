import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (4, 6), (5, 6), (6, 7)])

# Generate community sets determined by label propagation
communities = []
try:
    communities = list(nx.community.label_propagation_communities(G))
except nx.NetworkXError:
    print("Empty graph or graph with no edges")
    raise
    
# Print the community sets
print('Community Sets:')
for i, community in enumerate(communities):
    print(f'Community {i + 1}: {list(community)}')

# Visualize the communities
colors = ['r', 'g', 'b', 'y','m', 'c']
pos = nx.spring_layout(G)
for i, community in enumerate(communities):
    nx.draw_networkx(G, pos, nodelist=community, node_color=colors[i % len(colors)], with_labels=True, node_size=700)
plt.show()
