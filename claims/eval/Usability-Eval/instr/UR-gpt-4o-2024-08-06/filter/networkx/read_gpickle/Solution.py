import networkx as nx
import pickle

# Define a function to read a graph from a pickle file
def read_graph_from_pickle(file_path):
    with open(file_path, 'rb') as f:
        graph = pickle.load(f)
    return graph

# Example usage: specify the path to your pickle file
pickle_file_path = 'your_graph.pickle'

# Load the graph
G = read_graph_from_pickle(pickle_file_path)

# Now you can work with the graph object G
print("Nodes:", G.nodes())
print("Edges:", G.edges())
