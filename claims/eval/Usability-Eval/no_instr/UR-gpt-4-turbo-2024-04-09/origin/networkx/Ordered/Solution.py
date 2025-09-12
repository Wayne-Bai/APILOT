import networkx as nx

# Create an Ordered Graph
G = nx.OrderedGraph()
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_node('D')

# Create an Ordered DiGraph
DG = nx.OrderedDiGraph()
DG.add_edge('A', 'B')
DG.add_edge('A', 'C')
DG.add_edge('B', 'C')
DG.add_node('D')

# Create an Ordered MultiGraph
MG = nx.OrderedMultiGraph()
MG.add_edge('A', 'B')
MG.add_edge('A', 'B')  # multiple edges between the same nodes
MG.add_edge('A', 'C')
MG.add_node('D')

# Create an Ordered MultiDiGraph
MDG = nx.OrderedMultiDiGraph()
MDG.add_edge('A', 'B')
MDG.add_edge('A', 'B')  # multiple directed edges with same origin and destination
MDG.add_edge('B', 'A')
MDG.add_node('D')

# Print the nodes and edges in all graphs to see the order
print("Nodes in Ordered Graph:", list(G.nodes))
print("Edges in Ordered Graph:", list(G.edges))

print("\nNodes in Ordered DiGraph:", list(DG.nodes))
print("Edges in Ordered DiGraph:", list(DG.edges))

print("\nNodes in Ordered MultiGraph:", list(MG.nodes))
print("Edges in Ordered MultiGraph:", list(MG.edges))

print("\nNodes in Ordered MultiDiGraph:", list(MDG.nodes))
print("Edges in Ordered MultiDiGraph:", list(MDG.edges))
