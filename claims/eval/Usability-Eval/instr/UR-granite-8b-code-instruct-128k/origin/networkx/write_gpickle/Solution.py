
import pickle
import networkx as nx
# Create a graph
G = nx.Graph()
# Add nodes and edges to the graph
# ...
# Write the graph to a pickle file
with open('graph.pickle', 'wb') as f:
    pickle.dump(G, f)
