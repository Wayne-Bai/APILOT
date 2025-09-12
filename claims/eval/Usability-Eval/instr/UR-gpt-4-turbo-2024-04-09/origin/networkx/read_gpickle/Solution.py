import networkx as nx
import pickle

def read_graph_from_pickle(path):
    with open(path, 'rb') as file:
        graph = pickle.load(file)
    return graph

# Usage
graph_path = 'path_to_your_pickle_file.pkl'
graph = read_graph_from_pickle(graph_path)
print(graph.nodes())
print(graph.edges())
