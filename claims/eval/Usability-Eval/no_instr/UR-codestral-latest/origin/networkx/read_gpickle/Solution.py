# Import the necessary library
import networkx as nx
import pickle

# Open the pickle file for reading in binary mode
with open('graph_pickle', 'rb') as f:
    # Load the pickled data from the file
    graph_data = pickle.load(f)

# Let's assume that the pickled data is a dictionary containing two items, 'graph' and 'node_dict'
# 'graph' is the adjacency information for the graph and 'node_dict' is a dictionary of nodes
# These assumptions may vary depending on how the graph was pickled

# Restore the graph
G = nx.Graph(graph_data['graph'])

# Restore the nodes
nx.set_node_attributes(G, graph_data['node_dict'])

# Now you can work with the restored graph 'G'
