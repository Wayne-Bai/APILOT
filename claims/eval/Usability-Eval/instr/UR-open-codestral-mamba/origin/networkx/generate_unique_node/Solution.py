import networkx as nx

# initialize a graph
G = nx.Graph()

# add nodes with labels (unique node labels)
G.add_node('Node 1')
G.add_node('Node 2')
G.add_node('Node 3')

# add edges between nodes
G.add_edge('Node 1', 'Node 2')
G.add_edge('Node 2', 'Node 3')

# print the nodes and edges
print("Nodes of the graph: ")
print(G.nodes())
print("Edges of the graph: ")
print(G.edges())
