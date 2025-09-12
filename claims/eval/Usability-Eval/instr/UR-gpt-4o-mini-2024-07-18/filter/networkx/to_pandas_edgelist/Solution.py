import networkx as nx
import pandas as pd

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

# Convert the graph to a DataFrame
edge_list = pd.DataFrame(G.edges(data=True), columns=['Source', 'Target', 'Attributes'])

# Display the edge list DataFrame
print(edge_list)
