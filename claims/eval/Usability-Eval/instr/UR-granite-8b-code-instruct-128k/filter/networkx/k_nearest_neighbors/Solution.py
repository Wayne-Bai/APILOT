
import networkx as nx

def average_degree_connectivity(graph):
    avg_degree_conn = 0
    for node in graph.nodes():
        degree = graph.degree(node)
        avg_degree_conn += degree
    avg_degree_conn /= len(graph.nodes())
    return avg_degree_conn
