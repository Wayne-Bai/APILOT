
import networkx as nx

# Create a simple graph
G = nx.Graph()
G.add_nodes_from([1,2,3,4])
G.add_edges_from([(1,2),(2,3),(3,4)])

# Write the graph to YAML format
with open("graph.yaml", "w") as f:
    nx.write_yamlex(G, f)
