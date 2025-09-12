import networkx as nx

def generate_unique_node_label(G):
    # Ensure that the node labels are unique
    for node in G.nodes():
        if nx.is_directed(G):
            label = f"{node.name}_{G.out_degree(node)}"
        else:
            label = f"{node.name}_{G.degree(node)}"
        while label in G.nodes():
            label = f"{node.name}_{G.out_degree(node)}" if nx.is_directed(G) else f"{node.name}_{G.degree(node)}"
        G.nodes[node]['label'] = label
    return G
