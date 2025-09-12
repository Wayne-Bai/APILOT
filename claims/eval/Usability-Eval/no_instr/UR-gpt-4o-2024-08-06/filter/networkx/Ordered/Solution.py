import networkx as nx
from collections import OrderedDict

class OrderedGraph(nx.Graph):
    node_dict_factory = OrderedDict
    adjlist_dict_factory = OrderedDict
    edge_attr_dict_factory = OrderedDict

class OrderedDiGraph(nx.DiGraph):
    node_dict_factory = OrderedDict
    adjlist_dict_factory = OrderedDict
    edge_attr_dict_factory = OrderedDict

class OrderedMultiGraph(nx.MultiGraph):
    node_dict_factory = OrderedDict
    adjlist_dict_factory = OrderedDict
    edge_attr_dict_factory = OrderedDict

class OrderedMultiDiGraph(nx.MultiDiGraph):
    node_dict_factory = OrderedDict
    adjlist_dict_factory = OrderedDict
    edge_attr_dict_factory = OrderedDict

# Example usage for OrderedGraph
G = OrderedGraph()
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)
G.add_edge(2, 3)

print("Nodes:", list(G.nodes))
print("Edges:", list(G.edges))

# Example usage for OrderedDiGraph
D = OrderedDiGraph()
D.add_node(1)
D.add_node(2)
D.add_edge(1, 2)
D.add_edge(2, 3)

print("Directed Graph Nodes:", list(D.nodes))
print("Directed Graph Edges:", list(D.edges))
