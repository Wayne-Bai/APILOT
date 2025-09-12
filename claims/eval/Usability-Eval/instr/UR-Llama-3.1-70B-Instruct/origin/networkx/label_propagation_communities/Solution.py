import networkx as nx
import matplotlib.pyplot as plt

def generate_community_sets(G):
    """
    Generates community sets determined by label propagation.

    Parameters:
    G (networkx.Graph): Input graph.

    Returns:
    dict: A dictionary where the keys are the node labels and the values are the community labels.
    """
    return nx.algorithms.community.label_propagation_communities(G)

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6)])

# Generate community sets
社区 = generate_community_sets(G)

# Print the community sets
for i,社区 in enumerate(generate_community_sets(G)):
    print("Community", i+1, ":", 社区)

# Plot the graph with the community sets
community_dict = {node: i for i,grp in enumerate(generate_community_sets(G)) for node in grp}
pos = nx.spring_layout(G)
colors = ['r', 'g', 'b', 'y','m', 'c']
nx.draw_networkx(G, pos, node_color = [colors[community_dict[node]] for node in G.nodes], node_size = 200)
plt.show()
