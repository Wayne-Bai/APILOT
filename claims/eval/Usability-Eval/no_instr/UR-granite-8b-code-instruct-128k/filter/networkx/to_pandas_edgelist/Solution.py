import networkx as nx
import pandas as pd

# Create a graph
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')

# Convert the graph to a Pandas DataFrame
df = nx.to_pandas_edgelist(G)

# Print the DataFrame
print(df)
