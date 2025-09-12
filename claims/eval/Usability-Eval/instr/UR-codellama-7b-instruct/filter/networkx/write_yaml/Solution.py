
import networkx as nx

# create a directed graph object
G = nx.DiGraph()

# add nodes to the graph
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')

# add edges between nodes in the graph
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')

# write the graph to a YAML file
nx.write_yaml(G, path)
