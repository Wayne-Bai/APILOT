
import networkx as nx
import pickle

# create a DiGraph object
G = nx.DiGraph()

# add nodes and edges to the graph
G.add_nodes_from(['Alice', 'Bob', 'Charlie'])
G.add_edges_from([('Alice', 'Bob'), ('Bob', 'Charlie')])

# write the graph to a pickle file
with open('graph.pickle', 'wb') as f:
    pickle.dump(G, f)
