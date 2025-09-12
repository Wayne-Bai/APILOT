import networkx as nx
import pandas as pd

def edge_list_to_dataframe(graph):
    edge_list = graph.edges(data=True)
    return pd.DataFrame(edge_list, columns=['Source', 'Target', 'Attributes'])

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2, {'weight': 4}), (2, 3, {'weight': 5})])
edge_df = edge_list_to_dataframe(G)
print(edge_df)
