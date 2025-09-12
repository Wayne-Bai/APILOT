import networkx as nx
import yaml

def write_graph_yaml(G, file_name):
    data = {'nodes': list(G.nodes), 'edges': list(G.edges)}
    with open(file_name, 'w') as f:
        yaml.dump(data, f)

def read_graph_yaml(file_name):
    with open(file_name, 'r') as f:
        data = yaml.safe_load(f)
    G = nx.Graph()
    G.add_nodes_from(data['nodes'])
    G.add_edges_from(data['edges'])
    return G
