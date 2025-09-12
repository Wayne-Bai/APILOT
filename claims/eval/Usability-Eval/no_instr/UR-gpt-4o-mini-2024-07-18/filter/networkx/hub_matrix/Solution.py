import networkx as nx

def hits_hub_matrix(graph, max_iter=100, tol=1e-6):
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
        if norm == 0:
            norm = 1
        for node in authorities:
            authorities[node] /= norm
        
        # Update hub scores
        new_hubs = {node: 0.0 for node in graph.nodes()}
        for node in graph.nodes():
            for neighbor in graph.neighbors(node):
                new_hubs[node] += authorities[neighbor]

        # Normalize hub scores
        norm = sum(new_hubs.values())
        if norm == 0:
            norm = 1
        for node in new_hubs:
            new_hubs[node] /= norm

        # Check for convergence
        if all(abs(new_hubs[node] - hubs[node]) < tol for node in hubs):
            break
        
        hubs = new_hubs
    
    return hubs

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 4)])

hub_matrix = hits_hub_matrix(G)
print(hub_matrix)
