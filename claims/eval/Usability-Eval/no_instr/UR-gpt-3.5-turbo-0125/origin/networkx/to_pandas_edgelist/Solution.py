
import pandas as pd
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('C', 'A', weight=1)

# Get the edge list as a pandas DataFrame
edge_list = [(u, v, d['weight']) for u, v, d in G.edges(data=True)]
df_edge_list = pd.DataFrame(edge_list, columns=['source', 'target', 'weight'])

print(df_edge_list)
