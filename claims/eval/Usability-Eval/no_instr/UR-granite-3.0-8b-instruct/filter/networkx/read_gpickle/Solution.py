import networkx as nx

# Read the graph object from a pickle file
with open('graph.pkl', 'rb') as f:
    graph = nx.read_gpickle(f)

# Print the graph
print(graph.nodes())
print(graph.edges())
