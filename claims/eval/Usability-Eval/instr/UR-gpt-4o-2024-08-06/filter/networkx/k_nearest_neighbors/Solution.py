import networkx as nx

def compute_average_degree_connectivity(graph):
    # Calculate the average degree connectivity of the graph
    avg_deg_connectivity = nx.average_degree_connectivity(graph)
    return avg_deg_connectivity

# Example usage:
if __name__ == '__main__':
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0), (3, 4), (4, 5), (5, 6), (6, 4)])
    
    # Compute the average degree connectivity
    result = compute_average_degree_connectivity(G)
    print("Average Degree Connectivity:")
    for k, avg_neighbors in result.items():
        print(f"Degree {k}: Average Neighbors Degree {avg_neighbors}")
