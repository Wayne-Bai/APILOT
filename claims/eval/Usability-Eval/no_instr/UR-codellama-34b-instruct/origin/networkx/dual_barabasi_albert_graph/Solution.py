
import networkx as nx

# Set the number of nodes and edges for the graph
num_nodes = 100
num_edges = 500

# Create an empty graph object
G = nx.Graph()

# Add the nodes to the graph
for i in range(num_nodes):
    G.add_node(i)

# Add edges to the graph with preferential attachment
for i in range(num_edges):
    u, v = random.sample(G.nodes(), 2)
    G.add_edge(u, v)

# Print the graph
print(nx.draw_networkx(G, with_labels=True))
