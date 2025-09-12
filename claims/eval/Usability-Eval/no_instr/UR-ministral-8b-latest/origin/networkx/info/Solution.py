import networkx as nx

# Example use of the code
G = nx.Graph()

# Adding nodes and edges to the graph
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)

# Print summary of information for the graph G
print(nx.info(G))

# Print summary of information for a specific node n
n = 1
if n in G:
    print("Node '{}' is in the graph. Neighbor nodes: {}\n".format(n, list(G.neighbors(n))))
else:
    print("Node '{}' is not in the graph.".format(n))
