
import networkx as nx
def is_list_of_ints(lst):
    g = nx.Graph()
    for i in range(len(lst) - 1):
        g.add_edge(lst[i], lst[i+1])
    for node in g.nodes:
        if type(node) != int:
            return False
    return True
