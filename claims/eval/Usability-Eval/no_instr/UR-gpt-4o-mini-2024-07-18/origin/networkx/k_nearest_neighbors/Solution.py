import networkx as nx

def average_degree_connectivity(G):
    avg_connectivity = {}
    degrees = G.degree()
    
    # Create a dictionary to store nodes by their degree
    degree_dict = {}
    for node, degree in degrees:
        if degree not in degree_dict:
            degree_dict[degree] = []
        degree_dict[degree].append(node)
    
    # Calculate average nearest neighbor degree for each degree k
    for k in degree_dict:
        neighbors = []
        for node in degree_dict[k]:
            neighbors.extend(G.neighbors(node))
        
        # Calculate the degrees of neighbors and average them
        if neighbors:
            neighbor_degrees = [G.degree(neighbor) for neighbor in neighbors]
            avg_connectivity[k] = sum(neighbor_degrees) / len(neighbor_degrees)
        else:
            avg_connectivity[k] = 0
            
    return avg_connectivity

# Example usage:
G = nx.erdos_renyi_graph(100, 0.1)
avg_degree_conn = average_degree_connectivity(G)
print(avg_degree_conn)
