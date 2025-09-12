import networkx as nx
import numpy as np

# Create a simple graph with 6 nodes
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

# Define the community labels
labels = np.array([0, 0, 0, 1, 1, 1])

# Initialize the community sets
community_sets = [[] for _ in range(max(labels) + 1)]

# Label Propagation Algorithm
for _ in range(len(G.nodes)):
    new_labels = np.copy(labels)
    for i in range(len(G.nodes)):
        neighbors = list(G.neighbors(i + 1))
        label_counts = np.bincount(labels[neighbors])
        new_labels[i] = np.argmax(label_counts)
    labels = new_labels
    for i in range(len(G.nodes)):
        community_sets[labels[i]].append(i + 1)

# Print the community sets
for i, community_set in enumerate(community_sets):
    if community_set:
        print(f"Community {i}: {community_set}")
