import networkx as nx
import matplotlib.pyplot as plt

# Creates a random graph using Barabási–Albert preferential attachment model
# n: the number of nodes that the graph will contain
# m: number of edges to attach from a new node to existing nodes
n, m = 100, 5

# Create a graph using the Barabasi-Albert model
G = nx.barabasi_albert_graph(n, m)

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()
