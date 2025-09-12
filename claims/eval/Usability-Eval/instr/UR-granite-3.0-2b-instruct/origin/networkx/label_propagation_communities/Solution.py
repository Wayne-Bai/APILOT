import networkx as nx
from sklearn.cluster import LabelPropagation

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph

# Generate community sets using label propagation
label_propagation = LabelPropagation()
label_propagation.fit(G)
community_labels = label_propagation.labels_

# Print the community sets
for node, community in zip(G.nodes, community_labels):
    print(f"Node {node} belongs to community {community}")
