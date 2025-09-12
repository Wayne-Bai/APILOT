import networkx as nx
import pandas as pd

# Create a graph
graph = nx.Graph()

# Add edges to the graph
edges = [(1, 2), (2, 3), (3, 4), (4, 1)]

for edge in edges:
    graph.add_edge(*edge)

# Convert the edge list to a DataFrame
edge_df = pd.DataFrame(nx.edge_list(graph))

# Print the DataFrame
print(edge_df)
