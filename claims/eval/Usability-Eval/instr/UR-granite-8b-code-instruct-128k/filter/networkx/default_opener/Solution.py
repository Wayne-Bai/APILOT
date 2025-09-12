import networkx as nx
from networkx.algorithms import approximation

# Read in the graph
G = nx.read_graphml("graph.graphml")

# Find a minimum vertex cover
min_cover = approximation.vertex_cover(G)

# Open the file with the default program
import os
filename = "data.txt"
os.startfile(filename)
