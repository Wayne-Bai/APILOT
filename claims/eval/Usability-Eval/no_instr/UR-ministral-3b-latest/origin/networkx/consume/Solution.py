import networkx as nx

G = nx.Graph()

# Add nodes and edges
nodes = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Create a data stream/iterator
for node in nx.ego_network(G, 'A', undirected=True):
    print(node)
