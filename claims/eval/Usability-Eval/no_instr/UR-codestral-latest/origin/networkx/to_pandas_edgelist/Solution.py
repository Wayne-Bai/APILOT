import networkx as nx
import pandas as pd

# Create a sample graph
G = nx.Graph()

# Add edges
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])

# Convert the graph edge list to a Pandas DataFrame
edge_list = pd.DataFrame(list(G.edges()), columns=['Source', 'Target'])

print(edge_list)
