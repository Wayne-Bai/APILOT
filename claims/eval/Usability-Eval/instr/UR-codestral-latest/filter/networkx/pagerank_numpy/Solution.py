import networkx as nx

# Assuming G is your graph
pagerank = nx.pagerank(G)

# Print the PageRank of each node
for node, rank in pagerank.items():
    print(f"Node {node}: PageRank = {rank}")
