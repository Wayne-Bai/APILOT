import networkx as nx
import numpy as np

def scale_positions(G):
    pos = nx.spring_layout(G)  # Generate initial positions using spring layout
    max_pos = max(pos.values())  # Find the maximum position value
    min_pos = min(pos.values())  # Find the minimum position value
    scaled_pos = {node: (pos[node] - min_pos) / (max_pos - min_pos) for node in G.nodes()}  # Scale positions
    return scaled_pos
