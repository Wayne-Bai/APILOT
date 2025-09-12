import networkx as nx

def convert_dict_to_2d_array(dict_of_dicts):
    array = nx.to_numpy_matrix(dict_of_dicts)
    return array