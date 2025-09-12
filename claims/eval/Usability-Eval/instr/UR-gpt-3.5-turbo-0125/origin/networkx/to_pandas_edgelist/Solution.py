
import pandas as pd
import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=8)
G.add_edge('C', 'D', weight=5)

# Get the graph edge list as a Pandas DataFrame
edge_list = [(u, v, d['weight']) for u, v, d in G.edges(data=True)]
df = pd.DataFrame(edge_list, columns=['Source', 'Target', 'Weight'])

print(df)
