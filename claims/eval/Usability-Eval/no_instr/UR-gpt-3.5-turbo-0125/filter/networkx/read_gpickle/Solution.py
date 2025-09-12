
import networkx as nx
import pickle

# Read graph object in Python pickle format
with open('graph.pickle', 'rb') as f:
    G = pickle.load(f)

print(nx.info(G))
