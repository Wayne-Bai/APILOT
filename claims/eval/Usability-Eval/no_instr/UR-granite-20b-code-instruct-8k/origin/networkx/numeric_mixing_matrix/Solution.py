
import networkx as nx

def numeric_mixing_matrix(G):
    mixing_matrix = nx.attribute_mixing_matrix(G, attribute='weight')
    return mixing_matrix
