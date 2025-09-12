import networkx as nx
import pandas as pd

def graph_to_edge_list_df(G):
    # Extract edges from the graph
    edges = list(G.edges(data=True))
    
    # Create a DataFrame from the edge list
    edge_list_df = pd.DataFrame(edges, columns=['source', 'target', 'attributes'])
    
    return edge_list_df

# Example usage:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 4)])
# df = graph_to_edge_list_df(G)
# print(df)
