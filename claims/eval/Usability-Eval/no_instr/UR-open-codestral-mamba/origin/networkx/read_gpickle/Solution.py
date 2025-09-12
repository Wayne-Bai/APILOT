import networkx as nx
import pickle

def read_graph_from_pickle(file_path):
    with open(file_path, 'rb') as file:
        graph = pickle.load(file)
    return graph

# Replace 'your_file_path.pickle' with the path to your pickle file
file_path = 'your_file_path.pickle'
G = read_graph_from_pickle(file_path)
