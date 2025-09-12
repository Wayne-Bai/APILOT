import networkx as nx
import numpy as np

def scale_positions(G):
    positions = nx.spring_layout(G)
    scaled_positions = {node: np.array([pos[0] * 10, pos[1] * 10]) for node, pos in positions.items()}
    return scaled_positions
