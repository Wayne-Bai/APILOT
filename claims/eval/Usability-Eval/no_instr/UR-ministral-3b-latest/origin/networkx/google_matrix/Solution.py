import networkx as nx

G = nx.karate_club_graph()

# Draw the graph
import matplotlib.pyplot as plt
nx.draw(G, with_labels=True)
plt.show()
