import networkx as nx
from collections import OrderedDict

class OrderedGraph(nx.Graph):
    node_dict_factory = OrderedDict
    adjlist_dict_factory = OrderedDict

class OrderedDiGraph(nx.DiGraph):
    node_dict_factory = OrderedDict
    adjlist_dict_factory = OrderedDict

class OrderedMultiGraph(nx.MultiGraph):
    node_dict_factory = OrderedDict
    adjlist_dict_factory = OrderedDict

class OrderedMultiDiGraph(nx.MultiDiGraph):
    node_dict_factory = OrderedDict
    adjlist_dict_factory = OrderedDict

# Example usage:
# og = OrderedGraph()
# og.add_node(1)
# og.add_node(2)
# og.add_edge(1, 2)
# print(list(og.nodes))  # Output: [1, 2]
# print(list(og.edges))  # Output: [(1, 2)]
