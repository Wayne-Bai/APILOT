import networkx as nx
import pandas as pd

# Assuming G is your graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)

# Convert the edge list to a Pandas DataFrame
edge_list = list(G.edges())
df = pd.DataFrame(edge_list, columns=['Node1', 'Node2'])

print(df)
