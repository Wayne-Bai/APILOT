import networkx as nx
import numpy as np

def calculate_average_degree_connectivity(G):
    # Initialize a dictionary to store the sum of nearest neighbor degrees for each degree
    sum_degrees = {}
    
    # Initialize a dictionary to store the count of nodes for each degree
    count_degrees = {}
    
    # Iterate over all nodes in the graph
    for node in G.nodes():
        # Calculate the degree of the node
        node_degree = G.degree(node)
        
        # Initialize the sum of nearest neighbor degrees for the current degree if it does not exist
        if node_degree not in sum_degrees:
            sum_degrees[node_degree] = 0
            count_degrees[node_degree] = 0
        
        # Calculate the sum of degrees of the nearest neighbors
        neighbor_degrees = sum(G.degree(neighbor) for neighbor in G.neighbors(node))
        
        # Update the sum of nearest neighbor degrees for the current degree
        sum_degrees[node_degree] += neighbor_degrees
        
        # Update the count of nodes for the current degree
        count_degrees[node_degree] += 1
    
    # Calculate the average degree connectivity for each degree
    average_degree_connectivity = {
        degree: sum_degrees[degree] / count_degrees[degree] / degree
        for degree in sum_degrees
    }
    
    return average_degree_connectivity

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1,2), (1,3), (2,3), (2,4), (3,4), (4,5)])

# Calculate the average degree connectivity of the graph
average_degree_connectivity = calculate_average_degree_connectivity(G)

# Print the result
print(average_degree_connectivity)
