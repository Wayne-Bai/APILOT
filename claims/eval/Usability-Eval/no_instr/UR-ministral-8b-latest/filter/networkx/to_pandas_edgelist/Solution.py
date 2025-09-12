import networkx as nx
import pandas as pd

# Create a graph
G = nx.Graph()

# Add edges
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Convert the edge list to a DataFrame
edge_df = pd.DataFrame(list(G.edges(data=True)), columns=['source', 'target', 'data'])

# Drop 'data' column if not needed
# edge_df = edge_df.drop(columns=['data'])

# Print the DataFrame
print(edge_df)
