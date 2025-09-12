
import networkx as nx
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
nx.draw(G, with_labels=True)
