
import networkx as nx

# create a sample graph
G = nx.Graph()
G.add_node('Alice')
G.add_node('Bob')
G.add_edge('Alice', 'Bob', weight=3)

# write the graph to a pickle file
with open('graph.pkl', 'wb') as f:
    nx.write_pickle(G, f)
