import networkx as nx
import pickle

# Function to read a graph object from a pickle file
def read_graph_from_pickle(file_path):
    with open(file_path, 'rb') as file:
        graph = pickle.load(file)
    return graph

# Example usage
# graph = read_graph_from_pickle('path_to_your_pickle_file.pkl')
