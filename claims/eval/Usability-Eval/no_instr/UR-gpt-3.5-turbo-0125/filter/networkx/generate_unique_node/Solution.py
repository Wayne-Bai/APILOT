
import networkx as nx

G = nx.Graph()
G.add_node(1, label='unique_label_1')
G.add_node(2, label='unique_label_2')
# Add more nodes with unique labels as needed

print(G.nodes(data=True))
