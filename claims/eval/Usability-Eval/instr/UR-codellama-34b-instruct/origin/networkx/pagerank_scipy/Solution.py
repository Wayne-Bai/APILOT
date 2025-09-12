
import networkx as nx

# create a Graph object
G = nx.Graph()

# add nodes and edges to the graph
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')])

# calculate PageRank for each node in the graph
pageranks = nx.pagerank(G)

# print the results
for node, rank in pageranks.items():
    print(f"Node {node} has a PageRank of {rank}")
