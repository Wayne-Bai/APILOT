
import networkx as nx

def to_pandas_edgelist(graph):
    edgelist = nx.to_pandas_edgelist(graph)
    return edgelist
