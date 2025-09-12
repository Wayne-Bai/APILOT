import networkx as nx

def label_propagation_communities(G, max_iter=100, tol=1e-3):
    # Initialize node labels
    labels = {node: i for i, node in enumerate(G.nodes())}
    
    def update_label(node):
        # Count the labels of the neighbors
        label_count = {}
        for neighbor in G.neighbors(node):
            label = labels[neighbor]
            if label in label_count:
                label_count[label] += 1
            else:
                label_count[label] = 1
        
        # Find the most frequent label(s) among neighbors
        max_count = max(label_count.values())
        candidates = [label for label, count in label_count.items() if count == max_count]
        
        # Randomly select one of the most frequent labels
        return candidates[0] if len(candidates) == 1 else random.choice(candidates)
    
    # Iterate until labels converge or max iterations reached
    for i in range(max_iter):
        changes = 0
        for node in G.nodes():
            new_label = update_label(node)
            if labels[node] != new_label:
                labels[node] = new_label
                changes += 1
        if changes / len(G.nodes()) < tol:
            break
    
    # Group nodes by label
    communities = {}
    for node, label in labels.items():
        if label in communities:
            communities[label].add(node)
        else:
            communities[label] = {node}
    
    return list(communities.values())

# Example usage:
G = nx.karate_club_graph()
communities = label_propagation_communities(G)
for i, community in enumerate(communities):
    print(f"Community {i + 1}: {sorted(community)}")
