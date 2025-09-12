
import networkx as nx

def hits_authority_matrix(G):
    hits_tuple = nx.hits(G)
    return hits_tuple[0]
