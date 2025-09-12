import networkx as nx
from numpy import loadtxt

# Create a graph
G = nx.DiGraph()

# Read the input file to populate the graph with edges and weights
lines = loadtxt("input.txt", delimiter=",")
for line in lines:
    u, v, weight = line
    G.add_edge(u, v, weight=weight)

# Find the minimum-weight maximal matching
min_weight_matching = list(nx.max_weight_matching(G, maxcardinality=False))
