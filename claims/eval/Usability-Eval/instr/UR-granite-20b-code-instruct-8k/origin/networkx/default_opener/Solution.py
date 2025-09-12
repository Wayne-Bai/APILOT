import networkx as nx
import os

# Define the graph
G = nx.Graph()

# Add the filename as a node to the graph
G.add_node(filename)

# Open the filename using the system's default program
os.startfile(filename)
