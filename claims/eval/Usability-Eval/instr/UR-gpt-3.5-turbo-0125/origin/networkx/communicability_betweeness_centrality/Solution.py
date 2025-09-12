
import networkx as nx

def subgraph_communicability(G):
    node_pairs = [(node1, node2) for node1 in G.nodes() for node2 in G.nodes() if node1 != node2]
    communicability_dict = nx.communicability_exp(G)
    
    subgraph_communicability = {}
    for pair in node_pairs:
        node1, node2 = pair
        subgraph_communicability[pair] = communicability_dict[node1][node2]
    
    return subgraph_communicability
