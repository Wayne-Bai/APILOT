import networkx as nx
import os

# Open the filename using the system's default program
os.startfile(filename)

# Now, let's create a graph using networkx
G = nx.Graph()

# Add nodes to the graph
G.add_node('Node1')
G.add_node('Node2')

# Add edges to the graph
G.add_edge('Node1', 'Node2')

# Print the graph
print(G.nodes())
print(G.edges())
