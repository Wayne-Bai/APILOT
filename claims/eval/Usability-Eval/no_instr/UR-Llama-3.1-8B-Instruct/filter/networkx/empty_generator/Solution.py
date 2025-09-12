import networkx as nx
import matplotlib.pyplot as plt

# Create an empty Generator Graph object
G = nx.empty_graph()

print("Graph created with no nodes or edges.")
print("Type'enx.info(G)' to get information about the graph.")

# To get information about the graph
print(nx.info(G))

# To add nodes and edges
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1,2)
G.add_edge(2,3)

# To get neighbors of a node
print("Neighbors of Node 2: ", list(G.neighbors(2)))

# To draw the graph
nx.draw(G, with_labels=True)
plt.show()
