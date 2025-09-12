import networkx as nx
import numpy as np

def simrank_similarity(G, C=0.8, max_iters=100, epsilon=1e-4):
    # Initialize the simRank matrix with all nodes having simRank of 1 with themselves
    sim_prev = np.identity(len(G))
    for i in range(max_iters):
        sim = np.zeros((len(G), len(G)))
        for u, v in G.edges:
            # Calculate the simRank
            sim[u, v] = sim[v, u] = C * (sim_prev[list(G.neighbors(u))].sum() + sim_prev[list(G.neighbors(v))].sum()) / (len(list(G.neighbors(u))) * len(list(G.neighbors(v))))

        # Check if the difference is less than epsilon
        if np.allclose(sim, sim_prev, atol=epsilon):
            break
        sim_prev = np.copy(sim)
    return sim

# Create a graph using NetworkX
G = nx.Graph()
# Add your nodes and edges to the graph

# Convert the graph to a matrix representation for numpy operations
nodes = list(G.nodes)
indices = {node: i for i, node in enumerate(nodes)}

# Calculate SimRank
sim = simrank_similarity(G)

# Print the SimRank scores
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        print(f"SimRank score between nodes {nodes[i]} and {nodes[j]} is: {sim[i, j]}")
