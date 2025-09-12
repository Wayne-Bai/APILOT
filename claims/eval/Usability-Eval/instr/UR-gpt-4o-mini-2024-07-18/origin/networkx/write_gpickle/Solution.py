import networkx as nx
import pickle

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 4)])
G.nodes[1]['data'] = 'node 1 data'
G.edges[(1, 2)]['weight'] = 5

# Write the graph to a pickle file
with open('graph.pkl', 'wb') as f:
    pickle.dump(G, f)
