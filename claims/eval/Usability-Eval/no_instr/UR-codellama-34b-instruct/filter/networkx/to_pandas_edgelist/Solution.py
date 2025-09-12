
import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

# Convert the graph to a Pandas DataFrame
df = nx.to_pandas_dataframe(G, edge_attr=['weight'])

print(df)
