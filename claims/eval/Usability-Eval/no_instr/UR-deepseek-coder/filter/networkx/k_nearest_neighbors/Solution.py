import networkx as nx

def average_degree_connectivity(G):
    # Calculate the degree of each node
    degrees = dict(G.degree())
    
    # Calculate the average nearest neighbor degree for each degree k
    avg_connectivity = {}
    for node, degree in degrees.items():
        neighbors = G.neighbors(node)
        neighbor_degrees = [degrees[n] for n in neighbors]
        if neighbor_degrees:
            avg_connectivity[degree] = avg_connectivity.get(degree, 0) + sum(neighbor_degrees) / len(neighbor_degrees)
        else:
            avg_connectivity[degree] = 0
    
    # Normalize by the number of nodes with degree k
    degree_counts = {}
    for degree in degrees.values():
        degree_counts[degree] = degree_counts.get(degree, 0) + 1
    
    for degree in avg_connectivity:
        avg_connectivity[degree] /= degree_counts[degree]
    
    return avg_connectivity

# Example usage:
G = nx.karate_club_graph()
avg_connectivity = average_degree_connectivity(G)
print(avg_connectivity)
