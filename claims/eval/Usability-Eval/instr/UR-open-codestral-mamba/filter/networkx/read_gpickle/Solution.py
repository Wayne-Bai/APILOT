import networkx as nx
import pickle

# Load the graph object from the pickle file
with open('graph_object.pickle', 'rb') as handle:
    graph = pickle.load(handle)

# Now you can use the 'graph' object as you would any other networkx graph object
print(graph.number_of_nodes())
print(graph.number_of_edges())
