import networkx as nx

def compute_hits_hub_matrix(graph, max_iter=100, tol=1.0e-8):
    # Initialize hub scores
    hubs = {node: 1.0 for node in graph.nodes()}
    
    for _ in range(max_iter):
        # Calculate authority scores
        authorities = {node: 0.0 for node in graph.nodes()}
        for node in graph.nodes():
            for neighbor in graph.neighbors(node):
                authorities[neighbor] += hubs[node]

        # Normalize authority scores
        norm = sum(authorities.values())
        if norm > 0:
            authorities = {node: score / norm for node, score in authorities.items()}

        # Calculate new hub scores
        new_hubs = {node: 0.0 for node in graph.nodes()}
        for node in graph.nodes():
            for neighbor in graph.neighbors(node):
                new_hubs[node] += authorities[neighbor]

        # Normalize hub scores
        norm = sum(new_hubs.values())
        if norm > 0:
            new_hubs = {node: score / norm for node, score in new_hubs.items()}

        # Check for convergence
        if all(abs(new_hubs[node] - hubs[node]) < tol for node in graph.nodes()):
            break
        
        hubs = new_hubs

    return hubs

# Example usage
# G = nx.DiGraph()
# G.add_edges_from([(1, 2), (2, 3), (3, 1)])
# hub_scores = compute_hits_hub_matrix(G)
# print(hub_scores)
