import networkx as nx
import pandas as pd

# Sample graph creation
G = nx.Graph()
# Adding edges
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (1, 5)])

# Converting edges to a Pandas DataFrame
edge_list_df = pd.DataFrame(list(G.edges), columns=['Source', 'Target'])

print(edge_list_df)
