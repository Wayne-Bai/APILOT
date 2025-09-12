import networkx as nx
import pickle

# Create a sample graph
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)

# Write the graph to a pickle file
with open('graph.pickle', 'wb') as f:
    pickle.dump(G, f)

# To read the graph back from the pickle file
with open('graph.pickle', 'rb') as f:
    loaded_graph = pickle.load(f)
