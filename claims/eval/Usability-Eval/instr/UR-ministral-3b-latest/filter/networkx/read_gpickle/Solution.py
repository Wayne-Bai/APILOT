import networkx as nx
import pickle

# Read graph object in Python pickle format
graph_from_pickle = pickle.load(open('your_graph.pkl', 'rb'))

# Example of using the graph
print(graph_from_pickle.nodes())
print(graph_from_pickle.edges())
