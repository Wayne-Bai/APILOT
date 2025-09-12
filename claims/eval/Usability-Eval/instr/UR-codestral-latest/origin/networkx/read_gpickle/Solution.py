import networkx as nx
import pickle

# Load pickled graph
with open('graph.pickle', 'rb') as handle:
    G = pickle.load(handle)

# Check loaded graph information
print(type(G))
print(nx.info(G))
