import networkx as nx
import pandas as pd

# Create a graph
G = nx.Graph()

# Add some edges to the graph
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D')]
G.add_edges_from(edges)

# Generate the edge list as a Pandas DataFrame
edge_list_df = nx.to_pandas_edgelist(G)

print(edge_list_df)
