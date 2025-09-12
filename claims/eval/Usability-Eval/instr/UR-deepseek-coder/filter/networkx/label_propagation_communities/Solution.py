import networkx as nx

def label_propagation_communities(G):
    # Initialize labels to the node id
    labels = {node: node for node in G.nodes()}
    
    # Flag to indicate if the labels have stabilized
    stabilized = False
    
    while not stabilized:
        stabilized = True
        nodes = list(G.nodes())
        # Shuffle nodes to ensure randomness
        nx.utils.random.shuffle(nodes)
        
        for node in nodes:
            # Get the labels of the neighbors
            neighbor_labels = [labels[neighbor] for neighbor in G.neighbors(node)]
            
            # Count the occurrences of each label
            label_counts = {}
            for label in neighbor_labels:
                if label in label_counts:
                    label_counts[label] += 1
                else:
                    label_counts[label] = 1
            
            # Find the most frequent label
            max_count = max(label_counts.values())
            most_frequent_labels = [label for label, count in label_counts.items() if count == max_count]
            
            # Choose the label with the smallest id if there are ties
            new_label = min(most_frequent_labels)
            
            # Update the label of the node if it has changed
            if labels[node] != new_label:
                labels[node] = new_label
                stabilized = False
    
    # Extract communities from the labels
    communities = {}
    for node, label in labels.items():
        if label not in communities:
            communities[label] = set()
        communities[label].add(node)
    
    return list(communities.values())

# Example usage:
G = nx.karate_club_graph()
communities = label_propagation_communities(G)
print(communities)
