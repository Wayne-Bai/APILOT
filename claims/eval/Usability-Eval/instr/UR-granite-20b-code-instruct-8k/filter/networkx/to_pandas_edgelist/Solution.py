import pandas as pd
import networkx as nx

# Generate a graph edge list as a Pandas DataFrame
def generate_edge_list_df(graph):
    edges = nx.edges(graph)
    df = pd.DataFrame(edges, columns=['source', 'target'])
    return df
