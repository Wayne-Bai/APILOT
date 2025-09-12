import networkx as nx
import numpy as np

def convert_dict_to_2darray(d, mapping=None):
    G = nx.DiGraph(d)
    if mapping:
        relabel_map = {old_label: mapping[old_label] for old_label in G.nodes if old_label in mapping}
        G = nx.relabel_nodes(G, relabel_map)
    array = nx.to_numpy_array(G)
    return array

# Example usage
dict_of_dicts = {
    'a': {'b': 1, 'c': 2},
    'b': {'c': 3},
    'c': {'a': 4}
}

# Optional mapping dictionary
mapping = {'a': 0, 'b': 1, 'c': 2}

result_array = convert_dict_to_2darray(dict_of_dicts, mapping)
print(result_array)
