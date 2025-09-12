import networkx as nx
import pandas as pd

# Assuming G is your graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)

# Get the edge list from the graph
edge_list = list(G.edges())

# Convert the edge list to a Pandas DataFrame
df = pd.DataFrame(edge_list, columns=['Source', 'Target'])

# Print the DataFrame
print(df)
