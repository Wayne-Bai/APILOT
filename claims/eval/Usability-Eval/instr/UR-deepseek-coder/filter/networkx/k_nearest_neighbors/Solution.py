import networkx as nx

def average_degree_connectivity(G):
    # Compute the average degree connectivity for each degree k
    degree_connectivity = {}
    degrees = dict(G.degree())
    
    for node in G.nodes():
        degree = degrees[node]
        neighbors = G.neighbors(node)
        neighbor_degrees = [degrees[n] for n in neighbors]
        
        if degree not in degree_connectivity:
            degree_connectivity[degree] = []
        
        degree_connectivity[degree].extend(neighbor_degrees)
    
    # Calculate the average for each degree k
    avg_degree_connectivity = {k: sum(v) / len(v) for k, v in degree_connectivity.items()}
    
    return avg_degree_connectivity

# Example usage:
G = nx.karate_club_graph()
avg_connectivity = average_degree_connectivity(G)
print(avg_connectivity)
