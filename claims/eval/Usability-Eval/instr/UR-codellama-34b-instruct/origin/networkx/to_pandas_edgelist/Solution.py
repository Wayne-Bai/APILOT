import networkx as nx

def get_edge_list(G):
    return pd.DataFrame({
        "source": G.nodes(),
        "target": G.adjacency().keys()
    })
