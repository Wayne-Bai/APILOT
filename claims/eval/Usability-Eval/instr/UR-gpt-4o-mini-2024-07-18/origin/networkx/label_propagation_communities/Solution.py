import networkx as nx

def label_propagation_communities(graph):
    # Initialize the communities as a dictionary where every node is its own community
    communities = {node: i for i, node in enumerate(graph.nodes())}
    changed = True

    while changed:
        changed = False
        # Randomly shuffle the nodes to have a different order in each iteration
        for node in list(graph.nodes()):
            # Get the label counts of its neighbors
            neighbors = list(graph.neighbors(node))
            if not neighbors:
                continue
            
            label_count = {}
            for neighbor in neighbors:
                label = communities[neighbor]
                if label in label_count:
                    label_count[label] += 1
                else:
                    label_count[label] = 1

            # Find the label with the maximum count
            max_count = -1
            new_label = communities[node]
            for label, count in label_count.items():
                if count > max_count or (count == max_count and label < new_label):
                    max_count = count
                    new_label = label

            # Update the node's label if it has changed
            if new_label != communities[node]:
                communities[node] = new_label
                changed = True

    # Group nodes by their communities
    community_sets = {}
    for node, label in communities.items():
        if label not in community_sets:
            community_sets[label] = []
        community_sets[label].append(node)

    return list(community_sets.values())

# Example usage:
G = nx.erdos_renyi_graph(100, 0.05)
communities = label_propagation_communities(G)
print(communities)
