
import networkx as nx

def mixing_matrix(graph, attribute):
    mixing_matrix = nx.attribute_mixing_matrix(graph, attribute)
    return mixing_matrix
