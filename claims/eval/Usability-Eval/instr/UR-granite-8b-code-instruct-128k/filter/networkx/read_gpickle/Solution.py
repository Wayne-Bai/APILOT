import pickle
import networkx as nx

# Load the pickle file
with open('graph.pickle', 'rb') as f:
    graph = pickle.load(f)

# Print the nodes and edges of the graph
print("Nodes:")
for node in graph.nodes():
    print(node)

print("Edges:")
for edge in graph.edges():
    print(edge)
