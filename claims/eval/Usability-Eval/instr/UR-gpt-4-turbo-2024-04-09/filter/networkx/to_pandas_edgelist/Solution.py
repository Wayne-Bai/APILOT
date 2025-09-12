import networkx as nx
import pandas as pd

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Convert Graph to Pandas DataFrame
df = nx.to_pandas_edgelist(G)

print(df)
