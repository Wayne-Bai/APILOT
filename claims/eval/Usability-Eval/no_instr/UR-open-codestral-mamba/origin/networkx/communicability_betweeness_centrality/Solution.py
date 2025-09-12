import networkx as nx

def subgraph_communicability(G):
    nodes = list(G.nodes())
    comm = nx.communicability(G)
    subgraph_communicability = {}
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            subgraph_communicability[(nodes[i], nodes[j])] = comm[nodes[i]][nodes[j]]
    return subgraph_communicability
