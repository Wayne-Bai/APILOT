import networkx as nx
import pickle

# Create a sample graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (1, 3), (2, 3)])

# Write the graph to a pickle file
with open('graph.pickle', 'wb') as f:
    pickle.dump(G, f)

print("Graph has been written to graph.pickle")
