import networkx as nx

def read_graph_pickle(file_path):
    with open(file_path, 'rb') as file:
        graph = nx.read_gpickle(file)
    return graph
