import networkx as nx
import pickle

def read_graph_from_pickle(pickle_file_path):
    # Load the graph from a pickle file
    with open(pickle_file_path, 'rb') as pickle_file:
        graph = pickle.load(pickle_file)
    return graph

# Example usage:
# Replace 'your_pickle_file_path.pkl' with the path to your pickle file
graph = read_graph_from_pickle('your_pickle_file_path.pkl')
print(graph.nodes())
print(graph.edges())
