import networkx as nx

# Load the graph from a Python pickle file
with open('graph.pickle', 'rb') as f:
    G = nx.read_gpickle(f)
