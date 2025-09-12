import networkx as nx
# Read graph object from pickle file
with open('graph.pickle', 'rb') as f:
    graph = nx.read_gpickle(f)
# Print the graph object
print(graph.nodes(data=True))
print(graph.edges(data=True))
