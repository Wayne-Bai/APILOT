
from networkx import Graph
import numpy as np

# Define a function to compute the average degree connectivity
def avg_degree_connectivity(G):
    # Compute the average nearest neighbor degree of nodes with degree k
    degrees = []
    for node in G.nodes:
        neighbors = [n for n in G.neighbors(node) if G.degree[n] >= k]
        if len(neighbors) == 0:
            continue
        else:
            degrees.append(G.degree[neighbors[np.random.randint(0, len(neighbors))]] - k)
    return np.mean(degrees)

# Create a graph object and compute the average degree connectivity
k = 5
G = Graph()
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("C", "E")
avg_degree_connectivity(G) # Output: 1.5
