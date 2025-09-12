import networkx as nx
import matplotlib.pyplot as plt

def average_degree_connectivity(G):
    """
    Compute the average degree connectivity of graph.
    
    The average degree connectivity is the average nearest neighbor degree of nodes with degree k.
    
    Parameters:
    G (graph): NetworkX graph
    
    Returns:
    A dictionary with degree as keys and average nearest neighbor degree as values
    """
    degree_dict = dict(G.degree())
    avg_NN_k = {}
    
    for node in G.nodes():
        k = degree_dict[node]
        neighbors = list(G.neighbors(node))
        avg_k = sum(degree_dict[neighbor] for neighbor in neighbors) / len(neighbors)
        
        if k not in avg_NN_k:
            avg_NN_k[k] = []
        avg_NN_k[k].append(avg_k)
    
    for k in avg_NN_k:
        avg_NN_k[k] = sum(avg_NN_k[k]) / len(avg_NN_k[k])
    
    return avg_NN_k

# Create a sample graph
G = nx.erdos_renyi_graph(20, 0.2)

# Calculate average degree connectivity
avg_connectivity = average_degree_connectivity(G)

# Print the result
for k, avg_k in avg_connectivity.items():
    print(f"Average nearest neighbor degree of nodes with degree {k}: {avg_k}")

# Draw the graph
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
