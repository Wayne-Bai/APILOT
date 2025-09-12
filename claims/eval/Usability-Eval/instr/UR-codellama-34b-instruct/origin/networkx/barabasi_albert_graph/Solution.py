import networkx as nx
import random

# Define the parameters for the model
n = 100 # number of nodes
m = 10 # number of edges per node
p = 2 # exponent for the preferential attachment
q = 2 # exponent for the hubs

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
for i in range(n):
    G.add_node(i)

# Add edges to the graph using the Barabási–Albert model
for i in range(m):
    for j in range(i, n):
        if random.random() < p * q ** (G.degree[j] / m):
            G.add_edge(i, j)

# Output the graph
print(nx.info(G))
