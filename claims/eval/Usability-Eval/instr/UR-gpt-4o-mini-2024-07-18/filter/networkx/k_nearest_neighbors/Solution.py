import networkx as nx

def average_degree_connectivity(G):
    avg_connectivity = {}
    for node in G.nodes():
        degree = G.degree(node)
        neighbors = list(G.neighbors(node))
        if neighbors:
            avg_neighbor_degree = sum(G.degree(neighbor) for neighbor in neighbors) / len(neighbors)
            if degree in avg_connectivity:
                avg_connectivity[degree].append(avg_neighbor_degree)
            else:
                avg_connectivity[degree] = [avg_neighbor_degree]

    # Compute the average of each degree's values
    for degree in avg_connectivity:
        avg_connectivity[degree] = sum(avg_connectivity[degree]) / len(avg_connectivity[degree])
    
    return avg_connectivity

# Example usage:
G = nx.erdos_renyi_graph(100, 0.1)
result = average_degree_connectivity(G)
print(result)
