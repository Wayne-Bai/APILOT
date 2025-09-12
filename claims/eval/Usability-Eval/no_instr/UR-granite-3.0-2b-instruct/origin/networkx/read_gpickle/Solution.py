import networkx as nx

# Read graph object in Python pickle format
with open('graph.pickle', 'rb') as f:
    G = nx.read_gpickle(f)
