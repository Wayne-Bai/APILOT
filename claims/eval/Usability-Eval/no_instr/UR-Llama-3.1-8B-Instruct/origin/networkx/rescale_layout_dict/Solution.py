import networkx as nx
import matplotlib.pyplot as plt

def get_scaled_positions(pos, scale):
    scaled_positions = {}
    for node in pos:
        scaled_positions[node] = (pos[node][0] * scale, pos[node][1] * scale)
    return scaled_positions

# Example graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4], pos={'A': (0, 0), 'B': (3, 0), 'C': (1, 2), 'D': (2, 2)})
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Example positions keyed by node
pos = {'A': (0, 0), 'B': (3, 0), 'C': (1, 2), 'D': (2, 2)}

scale = 2

scaled_positions = get_scaled_positions(pos, scale)

nx.draw_networkx_nodes(G, scaled_positions, node_color='lightblue', alpha=0.5)
nx.draw_networkx_labels(G, scaled_positions, font_size=10, font_family='sans-serif')
nx.draw_networkx_edges(G, scaled_positions)

plt.axis('off')
plt.show()

print(scaled_positions)
