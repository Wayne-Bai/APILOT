import networkx as nx

def scale_positions(G):
    pos = nx.spring_layout(G)
    scaled_pos = {}
    for node in pos:
        x, y = pos[node]
        scaled_pos[node] = (x * 100, y * 100)
    return scaled_pos
