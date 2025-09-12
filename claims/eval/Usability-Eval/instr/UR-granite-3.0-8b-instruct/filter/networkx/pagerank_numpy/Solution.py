import networkx as nx

# Assuming G is your graph
# Compute the PageRank of the nodes in the graph
pr = nx.pagerank(G)

# Print the PageRank of each node
for node, rank in pr.items():
    print(f"Node {node}: {rank}")
