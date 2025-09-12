import networkx as nx
import pickle

# Create a new directed graph
G = nx.DiGraph()

# Add some nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Add some edges
G.add_edge(1, 2)
G.add_edge(2, 3)

# Serialize the graph to a pickle file
with open('graph.pkl', 'wb') as file:
    pickle.dump(G, file)

print('Graph has been serialized to graph.pkl')
